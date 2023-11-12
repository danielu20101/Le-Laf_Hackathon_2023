import { Component } from '@angular/core';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  viewDate = new Date();
  events = [];
  refresh = new Subject<void>();
  activeDayIsOpen = false;
}
