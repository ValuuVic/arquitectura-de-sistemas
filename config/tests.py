from datetime import timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class JWTAuthenticationTests(APITestCase):
    resources = (
        'clientes', 'direcciones', 'contactos', 'categorias', 'marcas',
        'productos', 'ordenes', 'detalles', 'facturas', 'bodegas',
        'movimientos', 'inventario', 'proveedores', 'servicios', 'contratos',
    )

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='jwt_test', password='Test-only-password-2026!'
        )

    def login(self):
        response = self.client.post(reverse('jwt_login'), {
            'username': 'jwt_test', 'password': 'Test-only-password-2026!'
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        return response.data

    def test_login_and_access_all_resources(self):
        tokens = self.login()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
        for resource in self.resources:
            with self.subTest(resource=resource):
                self.assertEqual(self.client.get(f'/api/{resource}/').status_code, 200)

    def test_all_resources_reject_anonymous_read_and_write(self):
        for resource in self.resources:
            for method in ('get', 'post', 'put', 'patch', 'delete'):
                url = f'/api/{resource}/'
                if method in ('put', 'patch', 'delete'):
                    url += '1/'
                with self.subTest(resource=resource, method=method):
                    response = getattr(self.client, method)(url)
                    self.assertEqual(response.status_code, 401)
                    self.assertTrue(response['WWW-Authenticate'].startswith('Bearer'))

    def test_invalid_credentials_and_inactive_login(self):
        response = self.client.post(reverse('jwt_login'), {
            'username': 'jwt_test', 'password': 'wrong'
        }, format='json')
        self.assertEqual(response.status_code, 401)
        self.user.is_active = False
        self.user.save(update_fields=['is_active'])
        response = self.client.post(reverse('jwt_login'), {
            'username': 'jwt_test', 'password': 'Test-only-password-2026!'
        }, format='json')
        self.assertEqual(response.status_code, 401)

    def test_refresh_and_verify(self):
        tokens = self.login()
        response = self.client.post(reverse('jwt_refresh'), {
            'refresh': tokens['refresh']
        }, format='json')
        self.assertEqual(response.status_code, 200)
        access = response.data['access']
        self.assertEqual(self.client.post(reverse('jwt_verify'), {
            'token': access
        }, format='json').status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        self.assertEqual(self.client.get('/api/productos/').status_code, 200)

    def test_invalid_expired_tampered_and_refresh_tokens_rejected(self):
        expired = AccessToken.for_user(self.user)
        expired.set_exp(from_time=timezone.now() - timedelta(minutes=5),
                        lifetime=timedelta(seconds=1))
        valid = str(AccessToken.for_user(self.user))
        header, payload, signature = valid.split('.')
        signature = ('A' if signature[0] != 'A' else 'B') + signature[1:]
        for token in ('invalid', str(expired), f'{header}.{payload}.{signature}',
                      str(RefreshToken.for_user(self.user))):
            with self.subTest(token_kind=token[:12]):
                self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
                self.assertEqual(self.client.get('/api/productos/').status_code, 401)

    def test_refresh_rejects_invalid_expired_and_access_tokens(self):
        expired = RefreshToken.for_user(self.user)
        expired.set_exp(from_time=timezone.now() - timedelta(days=2),
                        lifetime=timedelta(seconds=1))
        for token in ('invalid', str(expired), str(AccessToken.for_user(self.user))):
            with self.subTest(token_kind=token[:12]):
                self.assertEqual(self.client.post(reverse('jwt_refresh'), {
                    'refresh': token
                }, format='json').status_code, 401)

    def test_existing_tokens_reject_deactivated_user(self):
        tokens = self.login()
        self.user.is_active = False
        self.user.save(update_fields=['is_active'])
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
        self.assertEqual(self.client.get('/api/productos/').status_code, 401)
        self.client.credentials()
        self.assertEqual(self.client.post(reverse('jwt_refresh'), {
            'refresh': tokens['refresh']
        }, format='json').status_code, 401)

    def test_authenticated_crud_still_works(self):
        tokens = self.login()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {tokens['access']}")
        response = self.client.post('/api/categorias/', {
            'nombre': 'Prueba JWT', 'descripcion': 'Categoria de prueba', 'activa': True
        }, format='json')
        self.assertEqual(response.status_code, 201, response.data)
        url = f"/api/categorias/{response.data['id']}/"
        self.assertEqual(self.client.get(url).status_code, 200)
        self.assertEqual(self.client.patch(url, {'nombre': 'Actualizada'},
                                          format='json').status_code, 200)
        self.assertEqual(self.client.delete(url).status_code, 204)
