"""
These are a set of constant variables needed for the game to work across all .py files.
All values are in pixels, seconds, or degrees as appropriate.
"""

# --- Screen settings ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# --- Asteroid settings ---
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds between new asteroids
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# --- Player settings ---
PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300      # degrees per second
PLAYER_SPEED = 200           # pixels per second
PLAYER_SHOOT_SPEED = 500     # pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3  # seconds between shots

# --- Projectile settings ---
SHOT_RADIUS = 5