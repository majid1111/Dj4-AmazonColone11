import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projec.settings')
django.setup()
from faker import Faker
import random 
from product.models import Brand , Product





def seed_brand(n):
    fake = Faker()
    images = ['2.jpeg','3.jpeg','4.jpeg','5.jpg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg']
    for _ in range(n):
        Brand.objects.create(
          name = fake.name(),
          image = f'brands/{images[random.randint(0,12)]}'

        )

    print(f'Seed{n} Brands Successfully')
    


def see_product(n):
   fake = Faker()
   images = ['2.jpeg','3.jpeg','4.jpeg','5.jpg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg']
   flags = ['New','Sale','Features']
   for _ in range (n):
       Product.objects.create(
                    name = fake.name(),
          image = f'brands/{images[random.randint(0,12)]}',
          flag = flags[random.randint(0,2)],
          price = round(random.uniform(20.9,99.99),2),
          sku = random.randint(1000,10000000),
          subtitle = fake.text(max_nb_chars=250),
          description = fake.text(max_nb_chars=2000),
          quantity = random.randint(0,30),
          brand = Brand.objects.get(id=random.randint(1,122)),
 
       )


   print(f'Seed{n} product Successfully')


# seed_brand(5)

see_product(11) 