Projekt sterowania robotem poprzez klikniecia mysza, Jakub Zarczynski, Niodsr

## Opis projektu
Interfejs umożliwiający sterowanie robotem mobilnym (TurtleBot3) za pomocą kliknięć myszy na podglądzie z kamery. 
Kliknięcie w górnej połowie okna powoduje ruch do przodu, w dolnej - do tyłu.

## Wymagania
* Ubuntu 22.04
* ROS2 Humble
* OpenCV, cv_bridge

## Instalacja i uruchomienie
1. Skopiuj repozytorium do `~/ros2_ws/src`
2. Zbuduj projekt:
   ```bash
   cd ~/ros2_ws && colcon build
   source install/setup.bash
