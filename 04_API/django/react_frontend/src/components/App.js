import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  componentDidMount() {
    fetch("articles/api")
      .then(response => {
        if (response.status > 400) {
            return this.setState(() => {
                return { placeholder: "Something went wrong!"};
            });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
     <div>
        {this.state.data.map(articles => {
          return (
            <div key={article_id}>
                대분류: {articles.main_category}
                소분류: {articles.sub_category}
                제목: {articles.title}
                작성시간: {articles.writed_at}
                본문: {articles.content}
                기자: {articles.writer}
                언론사: {articles.press}
                URL: {articles.url}
            </div>
          );
        })}
      </div>
    );
  }
}

export default App;

const container = document.getElementById("api");
render(<App />, container);