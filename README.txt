Notes for National Park Service Info Kiosk webapp

Google Doc: https://docs.google.com/document/d/1jJSe3R4--DeefZ1An1vXuecV59ylH9EjrvcY_HmY1G8/edit

Spec:
1. Provides tools to assist users in finding specific information, such as state and designation filtering, name and keyword search.
2. Lists details about specific visitor centers, as well as nearby campgrounds.
3. Displays alerts, articles, events, and news releases about a selected destination.
4. Provides educational information about a selected destination, utilizing available lesson plans as well as relevant people and places associated with the location.

Optional:
1. When displaying information, utilize relevant symbols from the NPS Symbol Library to illustrate relevant items.
2. Utilize latitude and longitude data for map visualization or distance calculations.

Submission: 
In your submission, you will need to link to a live deployed website (e.g., Heroku, Github pages, etc.) and a link to your repository with code.

Graded On:
1. Meets Deliverables
2. Code Quality & Clarity
3. Creativity / Aesthetics (think UI/UX)

INFO:
API Key - Gyfs3mI6dUX4pKpcjcfevIVBLS5H8nytwe6L5Yue
Get started: https://www.nps.gov/subjects/developer/get-started.htm 
API Documentation: https://www.nps.gov/subjects/developer/api-documentation.htm#/
Challenge Home Page: https://www.mindsumo.com/contests/national-park-api

SETUP:
1. Home page (info) w/ navigation bar + search bar
	1. About
	2. News
	3. States
	4. Home
	5. (?) Maybe all parks?
2. All states --> parks in state
3. Parks in state --> park info
4. Park info page w/ general info, directions, etc... other stuff from API
	1. Campgrounds list (side-bar?)
	2. Learning info (???)
	3. Alerts
	4. News
	5. Articles
	6. Events
	7. OTHER
5. Campgrounds --> stuff from API
	1. 
6. ETC FIGURE OUT WHAT ELSE LATER

DEPLOYMENT BUGS/FIXES:
1. Crop images on home to same size
2. Auto-caps for state code
3. More noticible state/park codes
4. YT link on About leads to Twitter (oops)