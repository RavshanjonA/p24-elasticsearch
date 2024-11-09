import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

from blog.models import Category, Article, ARTICLE_TYPES


class Command(BaseCommand):
    help = "Generate fake users, categories, and articles"

    def add_arguments(self, parser):
        parser.add_argument(
            '--users', type=int, default=100, help='Number of fake users to create'
        )
        parser.add_argument(
            '--categories', type=int, default=10, help='Number of fake categories to create'
        )
        parser.add_argument(
            '--articles', type=int, default=1000, help='Number of fake articles to create'
        )

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Get the argument values
        user_count = kwargs['users']
        category_count = kwargs['categories']
        article_count = kwargs['articles']

        # Step 1: Create fake users
        self.stdout.write(self.style.NOTICE(f"Creating {user_count} fake users..."))
        users = []
        for _ in range(user_count):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )
            users.append(user)

        self.stdout.write(self.style.SUCCESS(f"Created {len(users)} users"))

        # Step 2: Create fake categories
        self.stdout.write(self.style.NOTICE(f"Creating {category_count} fake categories..."))
        categories = []
        for _ in range(category_count):
            category, created = Category.objects.get_or_create(
                name=fake.word(),
                description=fake.sentence()
            )
            categories.append(category)

        self.stdout.write(self.style.SUCCESS(f"Created {len(categories)} categories"))

        # Step 3: Create fake articles
        self.stdout.write(self.style.NOTICE(f"Creating {article_count} fake articles..."))
        for _ in range(article_count):
            # Select a random user as the author
            author = random.choice(users)

            # Randomly pick an article type
            article_type = random.choice([choice[0] for choice in ARTICLE_TYPES])

            # Generate the article
            article = Article.objects.create(
                title=fake.sentence(nb_words=6),
                author=author,
                type=article_type,
                content=fake.text(max_nb_chars=1000),
            )

            # Assign 1 to 3 random categories to the article
            selected_categories = random.sample(categories, random.randint(1, 3))
            article.categories.set(selected_categories)

            self.stdout.write(self.style.SUCCESS(f"Created article: {article.title}"))

        self.stdout.write(self.style.SUCCESS(f"Successfully created {article_count} fake articles"))
