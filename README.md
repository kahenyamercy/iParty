# 🎉 iPartyApp: Campus Party Planning Made Easy 🎉

Welcome to **iPartyApp**, the ultimate solution for effortless campus party planning. Whether you're an event organizer or an attendee, our app streamlines the entire process, making it easy to create, manage, and participate in events on your campus.

## Features

### 🚀 Key Features
- **Create Events**: Organizers can effortlessly create events with all necessary details.
- **Find Events**: Attendees can browse and search for upcoming events by campus or location.
- **Book and Pay**: Securely book a slot and make contributions directly through the app.
- **Notifications**: Receive instant notifications and confirmations via WhatsApp.
- **Campus-Specific Events**: View and manage events specific to your campus.

### 🎨 User Roles
- **Organizers**: Create and manage events, including setting the number of invitees and contribution amounts.
- **Attendees**: Book slots for events, view event details, and make contributions.

## 🏗️ Tech Stack
- **Backend**: Django & Django REST Framework
- **Frontend**: Django Templates with Bootstrap
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)
- **Payments**: M-Pesa integration via Daraja API
- **Messaging**: WhatsApp API for notifications

## 📦 Installation

### Prerequisites
- Python 3.8+
- Django 3.2+
- Virtualenv

### Setup
1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/ipartyapp.git
    cd ipartyapp
    ```

2. **Create a virtual environment**
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the app**
    Open your browser and navigate to `http://127.0.0.1:8000`.

## 🚀 Usage

### Creating an Event
1. Log in as an organizer.
2. Navigate to the events page and click "Create Event".
3. Fill in the event details, including the image, location, date, time, and required contributions.
4. Submit the form to create the event.

### Booking an Event
1. Log in as an attendee.
2. Browse the list of upcoming events.
3. Click on an event to view details and book a slot.
4. Make your contribution through the integrated payment gateway.
5. Receive a confirmation message via WhatsApp.

## 🛠️ Project Structure

iPartyApp/
│
├── ipartyapp/ # Project settings and configuration
│ ├── settings.py # Main settings file
│ ├── urls.py # URL declarations
│ └── wsgi.py # WSGI configuration
│
├── campus/ # Campus application
│ ├── migrations/ # Database migrations
│ ├── models.py # Data models
│ ├── views.py # View logic
│ └── urls.py # Campus URLs
│
├── events/ # Event application
│ ├── migrations/ # Database migrations
│ ├── models.py # Data models
│ ├── views.py # View logic
│ └── urls.py # Event URLs
│
├── users/ # User management application
│ ├── migrations/ # Database migrations
│ ├── models.py # Data models
│ ├── views.py # View logic
│ └── urls.py # User URLs
│
└── templates/ # HTML templates
├── base.html # Base template
├── campus/ # Campus templates
├── events/ # Event templates
└── users/ # User templates


## 🤝 Contributing

We welcome contributions to iPartyApp! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For any inquiries or support, please reach out to us at:
- Email: support@ipartyapp.com


## Authors

- **wamae-ndiritu**
    - Email: wamaejoseph392@gmail.com
    - Github: [wamae-ndiritu](https://github.com/wamae-ndiritu)
    - Twitter: [wamae-ndiritu](https://twitter.com/wamae-ndiritu)

- **kahenyamercy**
    - Email: kahenyamercy5@gmail.com
    - Github: [kahenyamercy](https://github.com/kahenyamercy)
    - Twitter: [kahenyamercy](https://twitter.com/kahenyamercy)

---

Thank you for choosing iPartyApp! We hope it makes your campus party planning a breeze. 🎉
