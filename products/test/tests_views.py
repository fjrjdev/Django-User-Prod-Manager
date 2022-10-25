from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from accounts.models import Account
from products.models import Product


class ProductTest(APITestCase):
    def setUp(self):
        self.base_URL = "/api/products/"
        self.user = Account.objects.create_user(
            username='seller',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
            is_seller=True
        )
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.product = Product.objects.create(
            description="Playstation do Yudi",
            price=5,
            quantity=15,
            seller_id=self.user.id
        )
        self.product2 = Product.objects.create(
            description="Bleybade Atomica",
            price=1000,
            quantity=1,
            seller_id=self.user.id
        )

    def test_somente_vendedor_pode_criar_produto(self):
        product = {
            "description": "Playstation do Japão",
            "price": 5,
            "quantity": 15
        }

        res = self.client.post(
            self.base_URL,
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 201)

        user = Account.objects.create_user(
            username='user',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
            is_seller=False
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.post(
            self.base_URL,
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 403)
        print("Somente vendedor pode criar produto. 💹")

    def test_somente_vendedor_do_produto_pode_atualizalo(self):
        product = {
            "description": "Pc é bem melhor",
        }
        res = self.client.patch(
            f'{self.base_URL}{str(self.product.id)}/',
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["description"], product["description"])

        user = Account.objects.create_user(
            username='user',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
            is_seller=False
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.patch(
            f'{self.base_URL}{str(self.product.id)}/',
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 403)
        print("Somente vendedor pode editar produto. 💹")

    def test_qualquer_um_pode_listar_filtrar_produtos(self):
        res = self.client.get(f"{self.base_URL}{self.product.id}/")

        self.assertEqual(res.status_code, 200)
        print("Qualquer um pode listar e filtrar produtos. 💹")

    def test_retorno_específico_para_listagem_criação(self):
        res = self.client.get(f"{self.base_URL}?page=1")

        self.assertEqual(res.status_code, 200)

        print("Retorno específico para listagem e criação.💹")

    def test_chaves_erradas(self):
        product = {
            "descriptiX": "Playstation do Japão",
            "prise": 5,
            "quaXtity": 15
        }
        res = self.client.post(
            self.base_URL,
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 400)
        print(f"Test Chaves erradas .💹")

    def test_criar_produto_com_quantidade_negativa(self):
        product = {
            "description": "Playstation do Japão",
            "price": 5,
            "quantity": -100
        }
        res = self.client.post(
            self.base_URL,
            product,
            format='json',
        )
        self.assertEqual(res.status_code, 400)
        print("Não pode criar produto com quantidade negativas.💹")
