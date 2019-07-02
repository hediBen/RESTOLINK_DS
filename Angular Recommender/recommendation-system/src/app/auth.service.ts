import { Injectable } from '@angular/core';
import {AngularFireAuth} from 'angularfire2/auth';
import * as firebase from 'firebase/app';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';
import {DashbordComponent} from './dashbord/dashbord.component';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  user: Observable<firebase.User>;
  userId: string;
  confiUrl = 'http://127.0.0.1:5000/CreateUser/' ;
  configGetUrl = 'http://127.0.0.1:5000/GetUser/';
  fetchIUsers = [];

  constructor(private fierbaseAuth: AngularFireAuth , private http: HttpClient) {
    this.user = this.fierbaseAuth.authState;
  }


  signup(email: string , password: string) {
    this.fierbaseAuth.auth.createUserWithEmailAndPassword(email, password).then(value => {
    console.log('Succes', value);
    this.createInterneUser(value.user.uid);
    }).catch(err => {console.log('Somthing went wrong', err.message); } );

  }

  login(email: string , password: string) {
    this.fierbaseAuth.auth.signInWithEmailAndPassword(email, password).then(value => {
      console.log( value.user.uid);
      this.userId = value.user.uid;

      console.log(this.fetchIUsers);
    }).catch(err => {console.log('Somthing went wrong', err.message); } );

  }

  logout() {
    this.fierbaseAuth.auth.signOut();
  }

  createInterneUser(uid: string){
    this.http.get(this.confiUrl + uid).subscribe(
      (response: any[] ) => console.log(response),
      (error) => console.log(error)
    );
  }




}
