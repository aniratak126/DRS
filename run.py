from CryptoProject import create_app
# from CryptoProject import db
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

    # with app.app_context():
    #    db.create_all()

# INSTRUCTIONS

# 1. File -> Settings -> Project: (kako vam se zove projekat) -> Python interpreter ->
# -> idete na plus -> i dodajete sve ove redom ->
# -> itsdangerous -> Flask-Bcrypt -> Flask-Login -> Flask-Mail -> Flask-WTF -> Mail -> Pillow -> PyJWT -> WTForms

# 2. Kada dodate sve to, idete na windows dugme, kucate "View Advanced System Settings", klik na dugme u donjem evom uglu :
# koje se zove "Environment Variables..."
# idete gornje dugme u sektoru User variables for (vase ime pc-a) koje se zove "New..."
# i dodate sledece
# SQLALCHEMY_DATABASE_URI / sqlite:///database.db
# SECRET_KEY / 5791628bb0b13ce0c676dfde280ba245
# EMAIL_USER / vasa email adresa
# EMAIL_PASS / vasa email lozinka

# restart pc
# zakomentarisati 6. liniju, odkomentarisati 2,8,9 i pokrenuti
# vratiti kako je bilo
# pokrenuti i kraj