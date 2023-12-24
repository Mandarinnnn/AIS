/**
 * import './App.css';
 * 
 * Стили по умолчанию App.css и index.css отключены, т.к. в данном приложении 
 * используется пакет со сторонними стилями UIKit (стили с префиксом uk-*).
 * 
 * Стили UIKit подключены через public/index.html:
 * 
 *   <link rel="stylesheet" href="%PUBLIC_URL%/uikit/css/uikit.min.css" />
 *   <script src="%PUBLIC_URL%/uikit/js/uikit.min.js"></script>
 *   <script src="%PUBLIC_URL%/uikit/js/uikit-icons.min.js"></script>
 *
 * Таким же образом можно подключать стили собственной разработки.
 * Подробнее о пакете UIKit см.: https://getuikit.com/docs/installation
 */
import React, { useState, useEffect} from "react";

import RobotMonitor from "./components/RobotMonitor";
import RobotForm from "./components/RobotForm";
import RobotAdd from "./components/RobotAdd";
import { CITY_NAMES } from "./components/constants";
import { ROBOT_IDs } from "./components/RobotMonitor";
/**
 * Корневой компонент App.js по умолчанию реализован в виде 
 * функционального компонента, для хранения состояния таких 
 * компонентов используется функция (хук) useState().
 * 
 * Зависимые компоненты (CityWeatherMonitor и CityWeatherForm) 
 * реализованы в виде классов и сохраняют состояние в специальном 
 * атрибуте state. Атрибут cityName={city} передаёт в данные компоненты
 * значение населённого пункта через объект props и соответствующий атрибут:
 * props.cityName
 * 
 * Подробнее о возможных реализациях React компонентов см.:
 * https://reactjs.org/docs/hooks-state.html
 * 
 */
 
 
 
 
function App() {
  const [id, setRobot] = useState('1');
  const [robot_ids, setOptions] = useState([]);
  //const [ROBOT_IDs, setROBOT] = useState([]);
  console.log(ROBOT_IDs);
  // Рендерим контент.
  // Функция map позволяет рендерить элементы массивов.
  
  useEffect(() => {
     //console.log(ROBOT_IDs);
  });
  
  useEffect(() => {
    // здесь можно получить данные с сервера или из другого источника
    const fetchData = async () => {
      // например, сделаем запрос на сервер для получения списка опций
     // console.log(ROBOT_IDs)
    };
    fetchData();
  }, []);
   
   
   
  
  return (
	<div class="bd">
      <div className="uk-section uk-section-muted">

        <div className="uk-margin uk-card uk-card-default uk-card-body uk-text-center">
          <h2>Выбрать робота</h2>
          <select className="select1" value={id} onChange={(e) => setRobot(e.target.value)}>
            {ROBOT_IDs.map((robotId) => <option value={robotId}>{robotId}</option>)}
          </select>
        </div>
        <h2>Информация о роботе</h2>
        <div className="center">
          <div className="uk-width-expand@m uk-card uk-card-default uk-card-body"><RobotMonitor robotId={id}/></div>
          <h2>Изменение режима работы</h2>
          <div className="robotform"><RobotForm robotId={id}/></div>
        </div>


        <div class="marginn">
        <h2>Добавление нового робота</h2>
        </div>
        <div className="robotadd"><RobotAdd/></div>
      </div>
    </div>
  );

}

export default App;
