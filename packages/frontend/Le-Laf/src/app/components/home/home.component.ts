import { Component, OnInit, TemplateRef, ViewChild } from '@angular/core';
import { CalendarEvent } from 'angular-calendar';
import { isSameDay, isSameMonth } from 'date-fns';
import { Subject } from 'rxjs';
import { EventService } from 'src/app/services/event.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  viewDate = new Date();
  events: CalendarEvent[] = [
    {
      start: this.viewDate,
      title: 'Meeting with HIghSchool Admin',
    },
  ];
  refresh = new Subject<void>();
  activeDayIsOpen = false;

  constructor(public eventService:EventService) {}

  ngOnInit(): void {
      this.eventService.getEvents().subscribe((data)=>{
        /// convert data into events
      })
  }

  dayClicked({ date, events }: { date: Date; events: CalendarEvent[] }): void {
    if (isSameMonth(date, this.viewDate)) {
      if (
        (isSameDay(this.viewDate, date) && this.activeDayIsOpen === true) ||
        events.length === 0
      ) {
        this.activeDayIsOpen = false;
      } else {
        this.activeDayIsOpen = true;
      }
      this.viewDate = date;
    }
  }

  handleEvent(action: string, event: CalendarEvent): void {
    console.log('action', action)
    console.log(event)
  }
}
