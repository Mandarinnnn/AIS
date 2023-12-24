import React from "react";
import axios from "axios";
import { API_URL} from "./constants";

class RobotAdd extends React.Component {

  constructor(props) {
    super(props);
    // устанавливаем состояние компонента по умолчанию
  
    this.state = {charge: '', position_x: '', position_y: '', state: '', loading_point_id: '', unloading_point_id: ''};
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
    console.log('POST Request to: ' + API_URL)
    // получаем Id населённого пункта из словаря и меняем состояние через встроенный метод класса React.Component setState
    // this.setState({carId: CAR_NAMES[this.props.carName]})
    event.preventDefault();   // необходимо, чтобы отключить стандартное поведение формы в браузере (AJAX)
    // формируем данные для отправки на сервер
    let data = {
	  id: 1,
	  charge: parseInt(this.state.charge),
	  position_x: parseInt(this.state.position_x),
	  position_y: parseInt(this.state.position_y),
      r_state: parseInt(this.state.state),
	  loading_point_id: parseInt(this.state.loading_point_id),
      unloading_point_id:parseInt(this.state.unloading_point_id)
    };
	console.log(data)
    // HTTP-клиент axios автоматически преобразует объект data в json-строку
    axios.post(API_URL, data, {
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
          <div>
              <div>
                  <table className="content-table">
                      <thead>
                      <tr>
                          <th>Уровень зарядки,%</th>
                          <th>Координата x</th>
                          <th>Координата y</th>
                          <th>Режим работы</th>
                          <th>Пункт загрузки</th>
                          <th>Пункт разгрузки</th>
                      </tr>
                      </thead>
                      <tr>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({charge: e.target.value})
                          }}/></td>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({position_x: e.target.value})
                          }}/></td>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({position_y: e.target.value})
                          }}/></td>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({state: e.target.value})
                          }}/></td>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({loading_point_id: e.target.value})
                          }}/></td>
                          <td><input type="text" class="inputtable" onChange={(e) => {
                              this.setState({unloading_point_id: e.target.value})
                          }}/></td>
                      </tr>
                  </table>
              </div>
              <input type="submit" value="Добавить" className="button"/>
          </div>
      </form>
    );
  }

}

export default RobotAdd;