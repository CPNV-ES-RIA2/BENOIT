import Container from './components/container';
import './output.css';
//import { createServer } from "miragejs"; // Un comment to use mock server



function App() {
  // Un comment to use mock server
  // createServer({
  //   routes() {

  //     this.get("/analyze", () => {
  //       return [
  //         {
  //           "name": "Nature",
  //           "confidence": 99.9991455078125
  //         },
  //         {
  //           "name": "Outdoors",
  //           "confidence": 99.9991455078125
  //         },
  //         {
  //           "name": "Scenery",
  //           "confidence": 99.9991455078125
  //         },
  //         {
  //           "name": "Landscape",
  //           "confidence": 99.94917297363281
  //         },
  //         {
  //           "name": "Water",
  //           "confidence": 97.77740478515625
  //         }
  //       ];
  //     })
  //   },
  // });
  return (
    <div className="App w-full text-center">
      <Container />
    </div>
  );
}

export default App;
