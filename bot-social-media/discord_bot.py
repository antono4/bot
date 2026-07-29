"""
Discord Bot - Auto moderation, welcome, dan commands
"""

import os
import logging
import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DiscordBot:
    def __init__(self, token: str, prefix: str = "!"):
        self.token = token
        self.prefix = prefix
        
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        
        self.bot = commands.Bot(command_prefix=prefix, intents=intents)
        self._setup_events()
        self._setup_commands()
        
        logger.info("Discord Bot initialized")
    
    def _setup_events(self):
        """Setup bot events"""
        
        @self.bot.event
        async def on_ready():
            logger.info(f"Bot logged in as {self.bot.user}")
            await self.bot.change_presence(
                activity=discord.Game("🤖 Automation Bot")
            )
        
        @self.bot.event
        async def on_member_join(member):
            """Welcome new member"""
            channel = member.guild.system_channel
            if channel:
                embed = discord.Embed(
                    title=f"Welcome {member.name}! 👋",
                    description=f"Welcome to {member.guild.name}!",
                    color=discord.Color.green()
                )
                embed.set_thumbnail(url=member.display_avatar.url)
                await channel.send(embed=embed)
        
        @self.bot.event
        async def on_message(message):
            """Auto moderation - block bad words"""
            if message.author.bot:
                return
            
            # Simple bad word filter (expand as needed)
            bad_words = ["badword1", "badword2"]  # Add actual bad words
            content = message.content.lower()
            
            if any(word in content for word in bad_words):
                await message.delete()
                await message.channel.send(
                    f"{message.author.mention} Keep it clean!",
                    delete_after=5
                )
            
            await self.bot.process_commands(message)
    
    def _setup_commands(self):
        """Setup bot commands"""
        
        @self.bot.command(name="ping")
        async def ping(ctx):
            """Check bot latency"""
            await ctx.send(f"🏓 Pong! Latency: {round(self.bot.latency * 1000)}ms")
        
        @self.bot.command(name="info")
        async def info(ctx):
            """Show server info"""
            guild = ctx.guild
            embed = discord.Embed(
                title=f"📊 {guild.name} Info",
                color=discord.Color.blue()
            )
            embed.add_field(name="Members", value=guild.member_count)
            embed.add_field(name="Channels", value=len(guild.channels))
            embed.add_field(name="Roles", value=len(guild.roles))
            embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
            await ctx.send(embed=embed)
        
        @self.bot.command(name="user")
        async def user(ctx, member: discord.Member = None):
            """Show user info"""
            member = member or ctx.author
            embed = discord.Embed(
                title=f"👤 {member.name}",
                color=member.color
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.add_field(name="ID", value=member.id)
            embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d"))
            embed.add_field(name="Roles", value=len(member.roles))
            await ctx.send(embed=embed)
        
        @self.bot.command(name="clear")
        @commands.has_permissions(manage_messages=True)
        async def clear(ctx, amount: int = 5):
            """Clear messages"""
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"🗑️ Cleared {amount} messages", delete_after=3)
        
        @clear.error
        async def clear_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send("❌ You don't have permission to clear messages!")
    
    def run(self):
        """Start the bot"""
        logger.info("Bot starting...")
        self.bot.run(self.token)


def main():
    from dotenv import load_dotenv
    load_dotenv()
    
    bot = DiscordBot(token=os.getenv('DISCORD_BOT_TOKEN'))
    bot.run()


if __name__ == "__main__":
    main()
