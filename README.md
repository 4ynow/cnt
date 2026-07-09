# 📇 cnt (Contact Manager CLI)

A lightweight, zero-dependency Python CLI tool to manage contacts with JSON storage, validation, duplicate checks, and a built-in change log.

---

## 🚀 Features

* **Zero Dependencies**: Uses only the Python standard library.
* **Input Validation**: Validates phone numbers and email formats automatically.
* **Duplicate Detection**: Blocks duplicate phone numbers or emails.
* **Tag Indexing**: Filter and search through contacts using custom tags.
* **Audit Trail**: Logs every add, edit, and delete action with a timestamp.

---

## 🛠️ Installation

```bash
# 1. Clone the repository
git clone https://github.com && cd cnt

# 2. Make the script executable
chmod +x contacts.py

# 3. Create a symlink to run 'cnt' from anywhere
sudo ln -s "\$(pwd)/contacts.py" /usr/local/bin/cnt
```

---

## 📖 Usage Examples

```bash
# View help and available commands
cnt --help

# 1. Add a new contact
cnt add --name "Alice" --phone "+123456789" --email "alice@example.com" --tags "friend,work"

# 2. List all contacts
cnt list

# 3. Search by name and tag
cnt search --name Alice --tag friend

# 4. Edit a contact by ID
cnt edit --id 1 --field phone --value "+987654321"

# 5. Delete a contact by ID
cnt delete 1

# 6. View the history log
cnt history
```

---

## 💾 Storage Architecture

Data is stored locally in a clean, human-readable flat JSON file:

```json
[
  {
    "id": 1,
    "name": "Alice",
    "phone": "+987654321",
    "email": "alice@example.com",
    "tags": ["friend", "work"],
    "created_at": "2026-07-09 19:15:32"
  }
]
```

---

## 🤝 Contributing

1. Fork the repo and create your feature branch (`git checkout -b feature/cool-feature`).
2. Commit your variations (`git commit -m 'feat: add export to csv'`).
3. Push to the branch (`git push origin feature/cool-feature`).
4. Open a Pull Request.

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for details.
