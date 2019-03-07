
import React, { Component } from 'react';    //  new
import ReactDOM from 'react-dom';   // import ReactDom
import axios from 'axios';    // new
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';




class App extends Component {
  constructor() {
    super();
    // new
    this.state = {
      users: [],
      username: 'test', // new
      email: 'test', // new
    };
    this.addUser = this.addUser.bind(this); //new
    this.handleChange = this.handleChange.bind(this);
  };

  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  };

  addUser(event) {
    event.preventDefault();
    // new
    const data ={
      username: this.state.username,
      email: this.state.email
    };
    //new
    axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
    .then((res) => {
      this.getUsers(); // new
      this.setState({username: '', email: ''});
    })
    .catch((err) => {console.log(err); });
  };

  // new
  componentDidMount(){
    this.getUsers();
  };
  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users }); }) //  new
    .catch((err) => { console.log(err); });
  }
  render() {
    return (
      <section className="section">
        <div className="containers">
          <div className="columns">
            <div className="column is-half">
            <br/>
            <h1 className="title is-1">All Users</h1>
            <hr/><br/>
            <AddUser
            username={this.state.username}
            email={this.state.email}
            addUser={this.addUser}
            handleChange={this.handleChange} //new
            />
            <br/><br/>
            <UsersList users={this.state.users}/>
          </div>
        </div>
      </div>
    </section>
    )
  }
};


// Use the render method from ReactDOM class to mount the App to the DOM to HTML
// element with an ID of root.
ReactDOM.render(
  <App />,
  document.getElementById('root')
);
