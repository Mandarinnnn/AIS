import React from "react";
import axios from "axios";
import {API_URL, MODE_IDs} from "./constants";
import {ROBOT_IDs} from "./RobotMonitor";


class RobotForm extends React.Component {

  constructor(props) {
    super(props);
    // устанавливаем состояние компонента по умолчанию
    this.state = {statee: '', robotId: this.props.robotId};
  }

  /**
   * Обновление данных на сервере (отправка HTTP PUT запроса).
   *
   * Данная функция вызывается при Submit формы.
   *
   * Конструкция updateData = (event) => {...} реализует публичную функцию, которую сразу можно
   * привязывать к событиям типа onChange, onSubmit и т.д.
   *
   * Подробнее об обработчиках событий в компонентах React см.: https://reactjs.org/docs/handling-events.html
   *
   * @param {*} event
   */
  updateData = (event) => {
    console.log('PUT Request to: ' + API_URL)
    // получаем Id населённого пункта из словаря и меняем состояние через встроенный метод класса React.Component setState
    this.setState({robotId: this.props.robotId})
    console.log(this.props.robotId)
    event.preventDefault();   // необходимо, чтобы отключить стандартное поведение формы в браузере (AJAX)
    // формируем данные для отправки на сервер
    //charge: 0,
    //position_x: 0,
    //position_y: 0,
    let data = {
      "id": this.props.robotId,
      "charge": 0,
      "position_x": 0,
      "position_y": 0,
      "r_state": parseInt(this.state.statee),
      "loading_point_id": 0,
      "unloading_point_id": 0
    };

    console.log(data)


    // HTTP-клиент axios автоматически преобразует объект data в json-строку
    axios.put(API_URL, data, {
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json;charset=UTF-8",
      },
    })
        .then(response => {
          console.log('Response: ' + response.status);
        }, error => {
          console.log(error);
          alert(error);
        });
  }

  render() {
    return (

        <form onSubmit={this.updateData} className="uk-form-stacked">
          <div className="robot-add">
            <table className="content-table">
              <thead>
              <tr>
                <th>1</th>
                <th>2</th>
                <th>3</th>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>Энергосберегающий</td>
                <td>Обычный</td>
                <td>Ускоренный</td>
              </tr>
              </tbody>
            </table>
            <input type="submit" value="Обновить" className="button"/>

            <label className="label">Режим работы:</label>
            <select className="select2" value={this.state.statee}
                    onChange={(e) => this.setState({statee: e.target.value})}>
              {MODE_IDs.map((mode) => <option value={mode}>{mode}</option>)}
            </select>



          </div>
        </form>
    );
  }

}

export default RobotForm;
