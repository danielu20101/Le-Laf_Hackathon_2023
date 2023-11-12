import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { ConfirmedEvent, OpenEvent } from '../models/event.model';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  events = new Subject<ConfirmedEvent[]>();

  openEvents = new Subject<OpenEvent[]>();

  constructor(public http:HttpClient) { }

  getEvents() {
    return this.events.asObservable();
  }

  fetchEvents(){
    this.http.get<ConfirmedEvent[]>(environment.url + 'events').subscribe(
      (data) => {
        this.events.next(data);
      },
      (error) => console.log(error)
    );
  }

  getOpenEvents() {
    return this.events.asObservable();
  }

  fetchOpenEvents() {
    this.http.get<OpenEvent[]>(environment.url + 'openEvents').subscribe(
      (data) => {
        this.openEvents.next(data);
      },
      (error) => console.log(error)
    );
  }
  
  calendarHelper(events:ConfirmedEvent[]){
    //loop through events and return calendar object
  }
  calendarHelperOpen(events:OpenEvent[]){
    
  }
}
