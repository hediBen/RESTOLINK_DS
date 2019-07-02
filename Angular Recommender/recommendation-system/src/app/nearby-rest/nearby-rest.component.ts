import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import {AuthService} from '../auth.service';
@Component({
  selector: 'app-nearby-rest',
  templateUrl: './nearby-rest.component.html',
  styleUrls: ['./nearby-rest.component.css']
})
export class NearbyRestComponent implements OnInit {

  constructor(private http: HttpClient , private  authservice: AuthService) { }
  fetchRestaurant: any[];
  configGetUrl = 'http://127.0.0.1:5000/GetUser/';
  nearUrl = 'http://127.0.0.1:5000/GetNearRest/';

  ngOnInit() {
    setTimeout( () => this.getUsers(this.authservice.userId), 2000);
  }

  getUsers(user: string) {

    this.http.get(this.configGetUrl + '\'' + user + '\'').subscribe(
      (response: any []) => this.getNearRestaurants(response[0]),
      error => console.log(error)

    );
  }
  getNearRestaurants(uid: string) {

    this.http.get(this.nearUrl + '\'' + uid + '\'').subscribe(
      (response: any []) => this.fetchRestaurant = response,
      error => console.log(error)

    );
  }

}
