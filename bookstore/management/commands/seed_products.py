from django.core.management.base import BaseCommand
from bookstore.models import Product

class Command(BaseCommand):
    help = 'Seed the database with initial products'

    def handle(self, *args, **options):
        products = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'price': 12.99,
                'description': 'A classic American novel set in the Jazz Age about wealth, love, and the American Dream.',
                'isbn': '978-0743273565',
                'category': 'Fiction',
                'stock_quantity': 50,
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'price': 14.99,
                'description': 'A gripping tale of racial injustice and childhood innocence in the American South.',
                'isbn': '978-0061120084',
                'category': 'Fiction',
                'stock_quantity': 45,
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'price': 13.99,
                'description': 'A dystopian novel about totalitarianism, surveillance, and individual freedom.',
                'isbn': '978-0451524935',
                'category': 'Fiction',
                'stock_quantity': 60,
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'price': 11.99,
                'description': 'A romantic novel of manners exploring marriage, social class, and love.',
                'isbn': '978-0141439518',
                'category': 'Romance',
                'stock_quantity': 55,
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'price': 10.99,
                'description': 'A coming-of-age novel about teenage angst and disillusionment.',
                'isbn': '978-0316769174',
                'category': 'Fiction',
                'stock_quantity': 40,
            },
            {
                'title': 'Sapiens',
                'author': 'Yuval Noah Harari',
                'price': 18.99,
                'description': 'A brief history of humankind from the Stone Age to modern times.',
                'isbn': '978-0062316097',
                'category': 'Non-Fiction',
                'stock_quantity': 35,
            },
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'price': 16.99,
                'description': 'An evidence-based guide to building better habits and breaking bad ones.',
                'isbn': '978-0735211292',
                'category': 'Self-Help',
                'stock_quantity': 70,
            },
            {
                'title': 'The Silent Patient',
                'author': 'Alex Michaelides',
                'price': 15.99,
                'description': 'A psychological thriller about a woman who commits a crime and never speaks again.',
                'isbn': '978-0525555377',
                'category': 'Thriller',
                'stock_quantity': 30,
            },
            {
                'title': 'Dune',
                'author': 'Frank Herbert',
                'price': 17.99,
                'description': 'An epic science fiction novel about politics, religion, and ecology on a desert planet.',
                'isbn': '978-0441013593',
                'category': 'Science Fiction',
                'stock_quantity': 25,
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'price': 13.99,
                'description': 'A fantasy adventure novel about a hobbit and his unexpected journey.',
                'isbn': '978-0547928227',
                'category': 'Fantasy',
                'stock_quantity': 50,
            },
            {
                'title': 'Educated',
                'author': 'Tara Westover',
                'price': 17.99,
                'description': 'A memoir about the author\'s journey from isolation to education and independence.',
                'isbn': '978-0399590504',
                'category': 'Biography',
                'stock_quantity': 40,
            },
            {
                'title': 'The Midnight Library',
                'author': 'Matt Haig',
                'price': 16.99,
                'description': 'A novel about life choices, second chances, and infinite possibilities.',
                'isbn': '978-0525559474',
                'category': 'Fiction',
                'stock_quantity': 45,
            },
            {
                'title': 'Circe',
                'author': 'Madeline Miller',
                'price': 17.99,
                'description': 'A reimagining of the goddess Circe from Greek mythology.',
                'isbn': '978-0393634632',
                'category': 'Fantasy',
                'stock_quantity': 35,
            },
            {
                'title': 'Thinking, Fast and Slow',
                'author': 'Daniel Kahneman',
                'price': 18.99,
                'description': 'A study of decision-making, psychology, and human behavior.',
                'isbn': '978-0374533555',
                'category': 'Non-Fiction',
                'stock_quantity': 30,
            },
            {
                'title': 'The Seven Husbands of Evelyn Hugo',
                'author': 'Taylor Jenkins Reid',
                'price': 17.99,
                'description': 'A glamorous tale of Old Hollywood filled with secrets and scandals.',
                'isbn': '978-0399586996',
                'category': 'Fiction',
                'stock_quantity': 50,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(
                isbn=product_data['isbn'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.title}'))
            else:
                self.stdout.write(f'Product already exists: {product.title}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded products!'))
