# Rocket Runners: Turbo Track Showdown

This is a 2D car racing game created with Pygame, inspired by classic arcade racers like Mario Kart.

## Features

-   **Physics-Based Vehicle Control:** Responsive vehicle handling with acceleration, braking, and drifting.
-   **Advanced AI Opponents:** AI racers with waypoint navigation and behavioral profiles.
-   **Interactive Hazards:** On-track obstacles like barriers, oil slicks, and mud pits.
-   **Power-Up System:** Collectable items like turbo boosts, shields, and missiles.
-   **Race Logic:** Lap and position tracking, with a full race flow from countdown to completion.
-   **Dynamic Effects:** Particle effects for collisions, drifting, and other in-game events.

## Project Structure

The project is organized into a modular architecture with a clear separation of concerns:

-   `main.py`: The primary application entry point, responsible for the main game loop, game state management, and event handling.
-   `config.py`: A centralized module for all static game constants.
-   `vehicle.py`: Defines the base `Vehicle` class, physics model, and `Player` class.
-   `ai.py`: Contains the `AIOpponent` class for AI logic.
-   `track.py`: Manages the track data, including the visual layout and waypoints.
-   `hazards.py`: Defines all interactive track hazards.
-   `powerups.py`: Defines all collectable power-ups.
-   `ui.py`: Renders the Heads-Up Display (HUD).
-   `effects.py`: Manages all visual particle effects.

## How to Run

1.  **Install Pygame:**
    ```bash
    pip install pygame
    ```
2.  **Run the Game:**
    ```bash
    python main.py
    ```

## Controls

-   **Up Arrow:** Accelerate
-   **Down Arrow:** Brake/Reverse
-   **Left/Right Arrows:** Steer
-   **Left Shift:** Drift
-   **Right Shift:** Use Power-up