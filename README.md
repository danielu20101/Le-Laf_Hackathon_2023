# Le-Laf_Hackathon_2023 - LVAIC_CONNECTS

## Team Members

- **Paolo Bartolucci**
  - Senior CSE Major
- **Daniel Unhuryan**
  - Senior CSE Major
- **Joe Bereswill**
  - Senior CSB Major

## Purpose

In the Bethlehem school district, multiple high schools are experiencing lower graduation rates, with students frequently losing interest in their academic pursuits. Through Lehigh Valley's Association of Independent Colleges, students can participate in community events with industry experts that can improve teaching skills, expand knowledge in specific disciplines, or teach about how to take on a leadership role. How can we raise student awareness for these school districts, and fortify LVAIC to serve as an even more powerful and engaging platform?

## Approach

We developed a platform allowing local Bethlehem High School admins to select days on calendars, and invite students to participate in 1:1 mentoring/advisory sessions with college students. High school admins submit a request that stays pending until a College Admin chooses to approve or deny a request. When multiple high school admins select requests that fall on the same time slot, the request that the college Admin approves gets scheduled across both calendars, and all other requests get rejected so High school admins can reselect another time slot.  

## Database ERD

![Database Entity Relationship Diagram](https://github.com/danielu20101/Le-Laf_Hackathon_2023/assets/62815005/1f4122a0-4988-4e14-aadd-d9584ac0a9ea)

## SetUp Instructions

## Setup Instructions

To get started with this project, please follow the instructions below:

### Frontend Setup

1. Clone the repository:
git clone <REPOSITORY-URL>

2. Change into the frontend directory:
cd frontend

3. Install npm dependencies:
npm install

4. Start the frontend service:
npm run start

### Backend Setup

5. Change into the backend directory:
cd backend

6. Create a virtual environment:
python3 -m venv env

7. Activate the virtual environment:
source env/bin/activate

8. Start the backend service with uvicorn:
uvicorn main:app --reload

The frontend and backend should now be up and running.

## Tech Stack

- Fast API
- Angular.js
- TypeScript
- JavaScript
