from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from accounts.models import Account


class AccountTestToken(APITestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='user',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
            is_seller=True
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_login_vendedor_retorna_token(self):
        seller_data_login = {
            "username": "user",
            "password": "password",
        }
        res_login = self.client.post(
            "/api/login/",
            seller_data_login,
            format='json'
        )

        self.assertEqual(res_login.status_code, 200)
        self.assertTrue(res_login.data['token'])
        print("Login vendedor retorna token. 💹")

    def test_somente_dono_atualiza_dados(self):
        user = Account.objects.get(username="user")
        res = self.client.patch(
            f"/api/accounts/{str(user.id)}/",
            {"first_name": "ronaldo"},
            format='json',
        )
        self.assertEqual(res.status_code, 200)
        print("Somente dono da conta pode atualizar dados.. 💹")


class AdmminAccountTestToken(APITestCase):
    def setUp(self):
        user = Account.objects.create_user(
            username='users',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_user_nao_pode_desativar(self):
        user = Account.objects.get(username="users")
        res = self.client.patch(
            f"/api/accounts/{str(user.id)}/",
            {"is_active": False},
            format='json',
        )
        self.assertEqual(res.status_code, 403)
        seller = Account.objects.get(username="users")
        self.assertEqual(seller.is_active, True)
        print("User não pode desativá-la. 💹")

    def test_somente_admininstrador_pode_desativar(self):
        admin = Account.objects.create_superuser(
            username='usersAdmin',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
        )
        token = Token.objects.create(user=admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        user = Account.objects.get(username="users")

        res = self.client.patch(
            f"/api/accounts/{str(user.id)}/",
            {"is_active": False},
            format='json',
        )
        self.assertEqual(res.status_code, 200)
        seller = Account.objects.get(username="users")
        self.assertEqual(seller.is_active, False)
        print("Somente admininstrador pode desaativá-la. 💹")

    def test_somente_admininstrador_pode_ativar(self):
        admin = Account.objects.create_superuser(
            username='usersAdmin',
            password='password',
            first_name="Bebeto",
            last_name="Fenomeno",
        )
        token = Token.objects.create(user=admin)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        user = Account.objects.get(username="users")

        res = self.client.patch(
            f"/api/accounts/{str(user.id)}/",
            {"is_active": True},
            format='json',
        )
        self.assertEqual(res.status_code, 200)
        seller = Account.objects.get(username="users")
        self.assertEqual(seller.is_active, True)
        print("Somente admininstrador pode ativá-la. 💹")


class AccountTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.baseURL = "/api/accounts/"
        cls.seller_data = {
            "username": "bebeto",
            "password": "1234",
            "first_name": "Bebeto",
            "last_name": "Fenomeno",
            "is_seller": True
        }
        cls.seller_data_wrong = {
            "username": True,
            "password": "1234",
            "first_name": "Bebeto",
        }
        cls.user_data = {
            "username": "romario",
            "password": "1234",
            "first_name": "Romario",
            "last_name": "Baixinho",
            "is_seller": False
        }
        cls.user_data_wrong = {
            "username": "romario",
            "first_name": "Romario",
            "last_name": 'dada',
            "is_seller": False
        }

    def test_create_vendedor(self):
        res = self.client.post("/api/accounts/", self.seller_data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            self.seller_data["username"],
            res.data['username'],
        )
        self.assertEqual(
            self.seller_data["first_name"],
            res.data['first_name'],
        )
        self.assertEqual(
            self.seller_data["last_name"],
            res.data['last_name'],
        )
        self.assertEqual(
            self.seller_data["is_seller"],
            res.data['is_seller'],
        )

        print("Criação de conta de vendedor. 💹")

    def test_create_user(self):
        res = self.client.post("/api/accounts/", self.user_data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(
            self.user_data["username"],
            res.data['username'],
        )
        self.assertEqual(
            self.user_data["first_name"],
            res.data['first_name'],
        )
        self.assertEqual(
            self.user_data["last_name"],
            res.data['last_name'],
        )
        self.assertEqual(
            self.user_data["is_seller"],
            res.data['is_seller']
        )

        print("Criação de conta de não vendedor. 💹")

    def test_create_vendedor_errado(self):
        res = self.client.post("/api/accounts/", self.seller_data_wrong)
        res_user = self.client.post("/api/accounts/", self.user_data_wrong)

        self.assertEqual(res.status_code, 400)

        self.assertEqual(res_user.status_code, 400)

        print("Chaves erradas em ambos os casos. 💹")

    def test_login_vendedor_nao_retorna_token(self):
        res = self.client.post("/api/accounts/", self.seller_data)

        seller_data_login = {
            "username": res.data["username"],
            "password": "12345"
        }

        res_login = self.client.post(
            "/api/login/",
            seller_data_login,
            format='json'
        )

        self.assertEqual(res_login.status_code, 400)
        self.assertEqual(
            res_login.data,
            {
                "non_field_errors": [
                    "Unable to log in with provided credentials."
                ]
            }
        )
        print("Login não vendedor retorna token. 💹")

    def teste_qualquer_um_pode_listar_usuarios(self):
        res = self.client.get("/api/accounts/newest/2/")

        self.assertEqual(res.status_code, 200)
        print("Qualquer um pode listar usuários. 💹")
