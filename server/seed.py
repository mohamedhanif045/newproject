from app import db, Bakery, BakedGood, app  # Import 'app' from your application module

def seed_data():
    with app.app_context():  # Wrap the database operations inside app context
        # Create sample bakeries
        bakery1 = Bakery(name="Awesome Bakery")
        bakery2 = Bakery(name="Best Bakery")
        bakery3 = Bakery(name="Freshly Baked")
        bakery4 = Bakery(name="Golden Oven Bakery")

        db.session.add_all([bakery1, bakery2, bakery3, bakery4])
        db.session.commit()

        # Create sample baked goods
        baked_good1 = BakedGood(name="Chocolate Cake", price=25.50, bakery_id=bakery1.id)
        baked_good2 = BakedGood(name="Croissant", price=3.75, bakery_id=bakery1.id)
        baked_good3 = BakedGood(name="Donut", price=1.50, bakery_id=bakery2.id)
        baked_good4 = BakedGood(name="Sourdough Bread", price=5.00, bakery_id=bakery3.id)
        baked_good5 = BakedGood(name="Apple Pie", price=15.00, bakery_id=bakery3.id)
        baked_good6 = BakedGood(name="Blueberry Muffin", price=2.25, bakery_id=bakery4.id)
        baked_good7 = BakedGood(name="Bagel", price=1.75, bakery_id=bakery4.id)
        baked_good8 = BakedGood(name="Cheesecake", price=30.00, bakery_id=bakery2.id)

        db.session.add_all([baked_good1, baked_good2, baked_good3, baked_good4, baked_good5, baked_good6, baked_good7, baked_good8])
        db.session.commit()

        print("Database seeded successfully with more data!")

if __name__ == '__main__':
    seed_data()
