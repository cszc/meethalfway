# Meet Halfway

Lauren Dyson, Christine Chung, Paul Mack, Leith McIndewar

## Slides
https://docs.google.com/presentation/d/1ZxHKsRMSGbwFMtpbUibnd6yFMMpW3dBG5YCZxZcA2YM/edit#slide=id.g107979916d_0_182

## Goal
Meet Halfway helps Chicagoans find a place to meet safely and securely. Our algorithm makes it easy to find a place to meet a friend or stranger that's convenient for both of you.

Given two starting locations, preferred modes of transit, and a desired type of location (coffe shop, restaurant, park, etc.), Meet Halfway finds a meeting destination with roughly equal travel times for both parties. Meeters have the option revealing their location to the other person or not; this way a meeting location can be agreed upon while protecting privacy.

## Use Cases
* As  a Craigslist seller, I want to arrange a meeting place with a potential buyer at a halfway point without revealing my location.
* As a U Chicago student, I want to meet my friend who lives on the north side at a coffee shop that’s convenient for both of us.
* As an online dating service user, I want to find a bar where I can meet my date without revealing my location.


## Data Sources
##### Distance Finding/Transporation Options
- [Google Maps & Distance Matrix API](https://developers.google.com/maps/?hl=en)

##### Meeting Locations, Business Types, Hours
- [Google Places](https://developers.google.com/places/?hl=en)
- [Yelp API](https://www.yelp.com/developers/documentation/v2/overview)

## Milestones/Timeline

<dl>
  <dt>Jan. 24</dt>
  <dd><b>Repo Created</b></dd>

  <dt>Jan 26 at 5pm</dt>
  <dd><b>Written Proposal</b>: One or two page proposal that describes the goal of the project and the source of data the group will use. It should also give a basic sketch of the work required to complete the project and a time-line for completing it. The proposal should also include a description of how the group plans to fulfill the third condition listed above.<dd>
    <dd><b>Proposal Presentation</b>:  Ten minute presentation that describes goals and plans.<dd>
    <dd><b>Wireframes completed</b><dd>

  <dt>Week of February 8</dt>
  <dd><b>Deliver MVP of distance identification</b>: Given two addresses and modes of transit, we can identify a meeting point that's roughly equal travel times for both (Main owner: Christine)<dd>
  <dd><b>Progress Check-in</b>: Each group will meet with an instructor for 15-20 minutes once during sixth week and again during eighth week to discuss the group’s progress, challenges, and plans.<dd>
  
  <dt>Week of February 16</dt>
  <dd><b>Deliver MVP of user interface</b>: Working prototype of frontend that allows user to input two locations / parameters at once (Main owner: Leith)<dd>
  
  <dt>Week of February 22</dt>
  <dd><b>Deliver MVP of location identification</b>: Given a meeting point, identify K locations meeting user requirements within a radius (Main owner: Lauren) <dd>
  <dd><b>Progress Check-in</b>: Each group will meet with an instructor for 15-20 minutes once during sixth week and again during eighth week to discuss the group’s progress, challenges, and plans.<dd>
  
  <dt>Week of February 29</dt>
  <dd><b>Deliver phase 2 MVP of user interface</b>: Working prototype of frontend that allows users to separately enter their locations and view a result (Main owner: Paul)<dd>

  <dt>Week of March 7</dt>
  <dd><b>Usability testing</b>: Working complete prototype that we can test with users<dd>
  
  <dt>Week of March 10</dt>
  <dd><b>Final Project Presentations (10th week)</b>: Each group must give a 15-20 minute presentation describing its project. The presentation should include descriptions of the project’s goal, the results obtained, and how the system is structured, along with anything interesting the group has learned in the process of building the system.</dd>
  
  <dt>March 15 at 5pm</dt>
  <dd><b>Completed Software</b>: Each submission should include a description of how to run the software and should be well documented. We must be able to compile and run your program(s) on a VM and we must be able to understand the structure of your code without undue effort.</dd>
</dl>


## New Things We're Using
- Data & Algorithm
  - Middle Finding Algorithm
  - [Google Maps API](https://developers.google.com/maps/?hl=en)
  - [Google Places API](https://developers.google.com/places/?hl=en)
  - [Yelp API](https://www.yelp.com/developers/documentation/v2/overview)
- Backend and Database
  - [Django](https://www.djangoproject.com/)
- Frontend 
  - [Bootstrap](http://getbootstrap.com/)
  - Javascript
  - CSS/HTML

## Old Things We're Using
- Python
- Backend
  - [SQLite](https://www.sqlite.org/)
