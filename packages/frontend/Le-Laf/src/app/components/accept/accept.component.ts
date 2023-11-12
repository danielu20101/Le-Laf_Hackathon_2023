import { Component } from '@angular/core';

@Component({
  selector: 'app-accept',
  templateUrl: './accept.component.html',
  styleUrls: ['./accept.component.css']
})
export class AcceptComponent {
  requests = [
    {
      id:1,
      requestor: "HSAdmin@school.edu",
      time: "10:00 AM - 11:00 AM",
      day: "Monday, November 2nd", 
      
    },
    {
      id:2,
      requestor: "HSAdmin2@school.edu",
      time: "10:00 AM - 11:00 AM",
      day: "Monday, November 9th",
    },
  ];
}
