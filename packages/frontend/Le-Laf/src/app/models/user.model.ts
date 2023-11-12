export type User = {
    userID:number;
    email:string;
    password:string;
    role:number;
}

export var DEFAULTUSER:User = {
    userID:-1,
    email:'',
    password:'',
    role:0
} 