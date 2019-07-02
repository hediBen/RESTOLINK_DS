import { Component, OnInit } from '@angular/core';

import {HttpClient} from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-recommendations',
  templateUrl: './recommendations.component.html',
  styleUrls: ['./recommendations.component.css']
})
export class RecommendationsComponent implements OnInit {
  constructor(private http: HttpClient , private  authservice: AuthService) { }
  CofUrl = 'http://127.0.0.1:5000/predictions/' ;
  fetchRestaurant: any[];
  configGetUrl = 'http://127.0.0.1:5000/GetUser/';
  rateUrl = 'http://127.0.0.1:5000/RateRestaurants/';
  ratedValue = null;
  nameUrl = 'http://127.0.0.1:5000/GetNameRest/';

  ngOnInit() {
    setTimeout( () => this.getUsers(this.authservice.userId), 2000);
  }
  getUsers(user: string) {

    this.http.get(this.configGetUrl + '\'' + user + '\'').subscribe(
      (response: any []) => this.getRecommendations(response[0]),
      error => console.log(error)

    );
  }



  getRestaurants(rest: string) {

    this.http.get(this.nameUrl + '\'' + rest + '\'').subscribe(
      (response: any []) => this.getRecommendations(response[0]),
      error => console.log(error)

    );
  }

  getRecommendations(uid: string) {

    this.http.get(this.CofUrl + uid).subscribe(
      (response: any []) => this.fetchRestaurant = response ,
      error => console.log(error)

    );
  }

  rateItem(recipeName) {
    this.http.get(this.rateUrl + recipeName + '/' + this.ratedValue + '/' + this.authservice.userId).subscribe(
      (response: any[]) => console.log(response),
      (error) => console.log(error));
  }

}
