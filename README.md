Tortoise ORM and Aerich 

# 1. virtualenv faollashtirilgan holatda:
```bash
pip install tortoise-orm aerich python-dotenv
```

# 2. aerich ni birinchi marta ishga tushirish:
```bash
aerich init -t db.DB_CONFIG
```

# 3. db yaratish:
```bash
aerich init-db
```

# 4. o'zgarishlar qo‘shilgach:
```bash
aerich migrate
```
```bash
aerich upgrade
```
