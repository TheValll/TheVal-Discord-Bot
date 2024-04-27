# TheVal Bot 🤖

## Overview ℹ️

TheVal Bot is a Discord bot designed to provide various useful commands and functionalities within a Discord server.

## Installation 🛠️

To use TheVal Bot, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain a Discord bot token from the Discord Developer Portal.
4. Create a `.env` file in the root directory of the project and add your Discord bot token as `DISCORD_TOKEN=<your-token-here>`.
5. Run the command `docker build --pull --rm -f "dockerfile" -t bot:latest "."`.
6. Run the command `docker compose -f "docker-compose.yml" up -d --build `.

## Installation on a Virtual Machine 🛠️

To deploy TheVal Bot on a virtual machine, follow these steps:

1. **Install Docker:** Docker is required to containerize and run the bot. Install Docker on your virtual machine by running the following commands:

   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   ```

2. **Install Docker Compose:** Docker Compose is used to define and run multi-container Docker applications. Install Docker Compose by running:

   ```bash
   sudo apt-get install -y docker-compose
   ```

3. **Clone the Repository:** Clone TheVal Bot repository to your virtual machine:

   ```bash
   git clone https://github.com/TheValll/TheVal-Discord-Bot
   cd TheVal-Discord-Bot
   ```

4. **Configure Environment Variables:** Create a `.env` file in the root directory of the project and add your Discord bot token as `DISCORD_TOKEN=<your-token-here>`.

5. **Build and Run the Docker Containers:** Build and run the Docker containers using the following commands:
   ```bash
   docker build --pull --rm -f "dockerfile" -t bot:latest "."
   docker-compose -f "docker-compose.yml" up -d --build
   ```

## Commands 💬

### Help ❓

- Description: Get help with available commands.
- Usage: `/help`

### YouTube 🎬

- Description: Get TheVal's YouTube channel link.
- Usage: `/youtube`

### Twitch 🎮

- Description: Get TheVal's Twitch channel link.
- Usage: `/twitch`

### Osu 🎵

- Description: Get TheVal's osu! profile link.
- Usage: `/osu`

### Colproz ✨

- Description: A tribute to Colproz.
- Usage: `/colproz`

### GitHub 🌐

- Description: Get the GitHub repository link.
- Usage: `/github`

## Usage 🚀

Once the bot is running and added to your Discord server, you can use the commands mentioned above to access various links and information provided by TheVal Bot.

Enjoy using TheVal Bot in your Discord server! If you have any questions
