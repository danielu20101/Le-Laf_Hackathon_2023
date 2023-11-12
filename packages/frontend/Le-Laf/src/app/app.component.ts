import { Component } from '@angular/core';
import { ModalService } from './services/modal.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Le-Laf';
  showBar = false;

  constructor(public modalService: ModalService) { }

  ngOnInit(): void {
    this.modalService.loggedInObservable().subscribe((data) => {
      this.showBar = data;
    })
  }

}
