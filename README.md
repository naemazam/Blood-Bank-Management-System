# Blood-Bank-Management-System

This **Blood Bank Management System Project** is accessible only to a certain **Blood Bank Organization**. The system requires the users to log their registered user credentials in order to gain access to the features and functionalities of the project. User credentials can be only registered by the **Super User/Admin** at **Django's Admin Site**. On this system, users can store, manage, and retrieve easily the blood donations along with some basic information about the donors. Here, the system automatically calculates the total available volume of blood in every blood group. Users can also store, manage, and retrieve records of the blood request. The request records automatically deduct the blood volume availability.

## **Features**

-   **Login and Logout**
-   **Dashboard**
    -   Displays the Blood Group Availability
-   **Blood Group Management**
    -   Add New Blood Group
    -   List All Blood Groups
    -   Update Blood Group Details
    -   Delete Blood Group
-   **Blood Donations Management**
    -   Add New Blood Donation
    -   List All Blood Donations
    -   View Blood Donation Details
    -   Update Blood Donation Details
    -   Delete Blood Donation
-   **Blood Request Management**
    -   Add New Blood Request
    -   List All Blood Requests
    -   View Blood Request Details
    -   Update Blood Request Details
    -   Delete Blood Request
-   **Automatically Calculate the Available Blood Volume**
-   **Profile Details Page**
-   **Update Profile Details**
-   **Update Account Password**

## **How to Run**
Before you get start please watch the video and follow it 

[watch Video](www,youtube.com) 

### **Download/Install the following**

-   **Python** _(_I used v3.9.1_)_
-   **PIP** _(_for python modules installation_)_

### Setup/Installation

1.  **Download** and  **Extract** the provided source code  `zip`  file.  _(download button is located below)_
2.  **Download** and  **Extract** the  `plugins`  files of this project at  **[Download](https://www.dropbox.com/s/uambi4bznj5i0ws/plugins.zip?dl=1)**. Move the extracted plugins folder inside the source code's  **static directory**
3.  **Open** your  **Terminal/Command Prompt**  window.  _(make sure to add "python" and "pip" in your environment variables)_
4.  **Change** the  **working directory**  to the extracted source code folder. i.e.  `cd C:\python\django_bbms`
5.  **Run** the following  **commands**:
    -   `pip install -r requirements.txt`
    -   `python manage.py migrate`
    -   `python manage.py runserver`
6.  Keep the terminals open and running.
7.  **Open** a  **web browser**  and  **browse** `http://localhost:8000/`  or  `http://127.0.0.1:8000/`

### Access Information for AdminSite

**SuperUser**  
Username:  **admin**  
Password:  **admin123**
