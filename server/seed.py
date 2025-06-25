from server.config import create_app, db
from server.models import User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username="admin")
    user.password = "adminpass"
    db.session.add(user)

    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Emma Watson", occupation="Actor")
    db.session.add_all([guest1, guest2])

    ep1 = Episode(date="2024-06-01", number=101)
    ep2 = Episode(date="2024-06-02", number=102)
    db.session.add_all([ep1, ep2])
    db.session.commit()

    app1 = Appearance(rating=5, guest_id=guest1.id, episode_id=ep1.id)
    app2 = Appearance(rating=4, guest_id=guest2.id, episode_id=ep1.id)
    db.session.add_all([app1, app2])

    db.session.commit()

    print("Database seeded!")
