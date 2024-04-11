# SkillCheckup

SkillCheckup is an online platform designed to conduct interview tests online, simulating real interview processes for aptitude, problem-solving, technical questions, and HR interviews. This repository contains the codebase for the SkillCheckup website built using Django.

## Features

- **User Authentication**: Allow users to register, log in, and manage their profiles.
- **Test Categories**: Organize tests into categories like aptitude, problem-solving, technical, HR, etc.
- **Question Bank Management**: Admin interface to add, edit, and delete questions with support for various question types.
- **Test Sessions**: Start and manage test sessions with time limits and randomized questions.
- **Real-Time Feedback**: Provide immediate feedback on answers during the test.
- **Score Calculation**: Automatically calculate and display scores at the end of each test.
- **Leaderboard and Rankings**: Display top scorers and allow users to compare their scores.
- **Review and Analytics**: Detailed analytics on test performance and progress tracking.
- **Notifications and Reminders**: Send email notifications for test reminders, results, and updates.
- **Interactive UI/UX**: User-friendly interface with intuitive navigation and responsive design.
- **Security Measures**: Prevent cheating and ensure secure user authentication practices.
- **Feedback and Support**: Allow users to provide feedback and offer support through a FAQ section.

## Installation

1. Clone the repository:

   git clone 'https://github.com/Praveensv11/SkillCheckup.git'
   cd SkillCheckup
   
   
2. Set up database:
   
   python manage.py migrate

3. Create a superuser:

   python manage.py createsuperuser

4. Run the development server:

   python manage.py runserver

5. Access the website at http://127.0.0.1:8000/ and log in with the superuser credentials to start managing the platform.

## Contributing

Contributions are welcome! If you'd like to contribute to SkillCheckup, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
