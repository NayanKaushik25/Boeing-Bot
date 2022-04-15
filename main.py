import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
  print("Bot is currently online!")


@client.command()
async def BoeingInfo(ctx):
  embed=discord.Embed(title="Boeing",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Boeing Company (/ˈboʊɪŋ/) is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, telecommunications equipment and missiles worldwide.",inline=True)
  embed.add_field(name="Founder",value="William E Boeing",inline=False)
  embed.add_field(name="Founded",value="July 15th, 1916",inline=True)
  embed.add_field(name="Revenue",value="$62.29 Billion (2021)",inline=True)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/2004-09-14_1680x3000_chicago_boeing_building.jpg/220px-2004-09-14_1680x3000_chicago_boeing_building.jpg")
  await ctx.send(embed=embed)
  
  
@client.command()
async def B707(ctx):
  embed=discord.Embed(title="Boeing 707",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Boeing 707 is an American long-range narrow-body airliner that was developed and produced by Boeing Commercial Airplanes, its first jetliner.",inline=False)
  embed.add_field(name="Produced",value="1956-1978",inline=False)
  embed.add_field(name="Engines",value="Pratt & Whitney JT3D",inline=False)
  embed.add_field(name="First Operator",value="Pan Am",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Boeing_707-321B_Pan_Am_Freer.jpg/300px-Boeing_707-321B_Pan_Am_Freer.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B717(ctx):
  embed=discord.Embed(title="Boeing 717",color=discord.Colour.purple())
  embed.add_field(name="Basic Info",value="The Boeing 717 is an American twin-engine, single-aisle jet airliner, developed for the 100-seat market. The five-abreast airliner was designed and originally marketed by McDonnell Douglas as the MD-95, a derivative of the DC-9 family.",inline=False)
  embed.add_field(name="Produced",value="1998-2006",inline=False)
  embed.add_field(name="Engines",value="BMW Rolls Royce BR700",inline=False)
  embed.add_field(name="First Operator",value="AirTran",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/AirTran_Boeing_717_Airwim-1.jpg/220px-AirTran_Boeing_717_Airwim-1.jpg")
  await ctx.send(embed=embed)
  

@client.command()
async def B720(ctx):
  embed=discord.Embed(title="Boeing 720",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="The Boeing 720 is an American narrow-body airliner produced by Boeing Commercial Airplanes. Announced in July 1957 as a 707 derivative for shorter flights from shorter runways, the 720 first flew on November 23, 1959.",inline=False)
  embed.add_field(name="Produced",value="1958-1967",inline=False)
  embed.add_field(name="Engines",value="Pratt and Whitney JT3D",inline=False)
  embed.add_field(name="First Operator",value="United Airlines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Cyprus_Airways_Boeing_720B_G-BCBB_LHR_1978-8-24.png/300px-Cyprus_Airways_Boeing_720B_G-BCBB_LHR_1978-8-24.png")
  await ctx.send(embed=embed)

@client.command()
async def B727(ctx):
  embed=discord.Embed(title="Boeing 727",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Boeing 727 is an American narrow-body airliner that was developed and produced by Boeing Commercial Airplanes. It is the only trijet ever developed by Boeing.",inline=False)
  embed.add_field(name="Produced",value="1962-1984",inline=False)
  embed.add_field(name="Engines",value="Pratt & Whitney JT8D",inline=False)
  embed.add_field(name="First Operator",value="Eastern Air Lines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/B-727_Iberia_%28cropped%29.jpg/300px-B-727_Iberia_%28cropped%29.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B737(ctx):
  embed=discord.Embed(title="Boeing 737",color=discord.Colour.green())
  embed.add_field(name="Basic Info",value="The Boeing 737 is a narrow-body aircraft produced by Boeing at its Renton Factory in Washington. Developed to supplement the Boeing 727 on short and thin routes, the twinjet retains the 707 fuselage cross-section and nose with two underwing turbofans.")
  embed.add_field(name="Produced",value="1966-Present",inline=False)
  embed.add_field(name="First Operator",value="Lufthansa",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/South_African_Airlink_Boeing_737-200_Advanced_Smith.jpg/300px-South_African_Airlink_Boeing_737-200_Advanced_Smith.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B747(ctx):
  embed=discord.Embed(title="Boeing 747",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="The Boeing 747 is a large, long-range wide-body airliner designed and manufactured by Boeing Commercial Airplanes in the United States. After introducing the 707 in October 1958, Pan Am wanted a jet 2+1⁄2 times its size, to reduce its seat cost by 30% to democratize air travel. In 1965, Joe Sutter left the 737 development program to design the 747, the first twin aisle airliner. In April 1966, Pan Am ordered 25 Boeing 747-100 aircraft and in late 1966, Pratt & Whitney agreed to develop its JT9D engine, a high-bypass turbofan. On September 30, 1968, the first 747 was rolled out of the custom-built Everett Plant, the world's largest building by volume. The first flight took place on February 9, 1969, and the 747 was certified in December of that year. It entered service with Pan Am on January 22, 1970. The 747 was the first airplane dubbed Jumbo Jet, the first wide-body airliner.",inline=False)
  embed.add_field(name="Produced",value="1968-2022",inline=False)
  embed.add_field(name="Engines",value="Pratt and Whitney JT9D",inline=False)
  embed.add_field(name="First Operator",value="Pan Am")
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Northwest_Airlines_Boeing_747-400_Spijkers.jpg/220px-Northwest_Airlines_Boeing_747-400_Spijkers.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B757(ctx):
  embed=discord.Embed(title="Boeing 757",color=discord.Colour.orange())
  embed.add_field(name="Basic Info",value="The Boeing 757 is an American narrow-body airliner designed and built by Boeing Commercial Airplanes. The then-named 7N7, a twinjet successor for the 727 (a trijet), received its first orders in August 1978. The prototype completed its maiden flight on February 19, 1982 and it was FAA certified on December 21, 1982.",inline=False)
  embed.add_field(name="Produced",value="1981-2004",inline=False)
  embed.add_field(name="Engines",value="Rolls Royce RB211",inline=False)
  embed.add_field(name="First Operator",value="Eastern Airlines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/a/a6/Monarch_Airlines_Boeing_757-2T7_Innsbruck_Wedelstaedt.jpg")
  await ctx.send(embed=embed)

  
  
@client.command()
async def B767(ctx):
  embed=discord.Embed(title="Boeing 767",color=discord.Colour.green())
  embed.add_field(name="Basic Info",value="The Boeing 767 is an American wide-body aircraft developed and manufactured by Boeing Commercial Airplanes. The aircraft was launched as the 7X7 program on July 14, 1978, the prototype first flew on September 26, 1981, and it was certified on July 30, 1982. The original 767-200 entered service on September 8, 1982 with United Airlines, and the extended-range 767-200ER in 1984. It was stretched into the 767-300 in October 1986, followed by the 767-300ER in 1988, the most popular variant. The 767-300F, a production freighter version, debuted in October 1995. It was stretched again into the 767-400ER from September 2000.",inline=False)
  embed.add_field(name="Produced",value="1981-Present",inline=False)
  embed.add_field(name="Engines",value="Rolls Royce RB211",inline=False)
  embed.add_field(name="First Operator",value="United Airlines",inline=False)
  embed.set_thumbnail(url="https://i.pinimg.com/originals/8a/8a/38/8a8a382c5baa0e14d36d5ec97b3783ee.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B777(ctx):
  embed=discord.Embed(title="Boeing 777",color=discord.Colour.red())
  embed.add_field(name="Basic Info",value="The Boeing 777, commonly referred to as the Triple Seven, is an American long-range wide-body airliner developed and manufactured by Boeing Commercial Airplanes. It is the world's largest twinjet. The 777 was designed to bridge the gap between Boeing's other wide body airplanes, the twin-engined 767 and quad-engined 747, and to replace older DC-10s and L-1011 trijets. Developed in consultation with eight major airlines, with a first meeting in January 1990, the program was launched on October 14, 1990, with an order from United Airlines. The prototype was rolled out on April 9, 1994, and first flew on June 12, 1994. The 777 entered service with the launch customer, United Airlines, on June 7, 1995. It is the company's first aircraft to feature fly by wire technology.",inline=False)
  embed.add_field(name="Produced",value="1993-Present",inline=False)
  embed.add_field(name="Engines",value="General Electric GE90",inline=False)
  embed.add_field(name="First Operator",value="United Airlines",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Cathay_Pacific_Boeing_777-200%3B_B-HNL%40HKG.jpg/300px-Cathay_Pacific_Boeing_777-200%3B_B-HNL%40HKG.jpg")
  await ctx.send(embed=embed)


@client.command()
async def B787(ctx):
  embed=discord.Embed(title="Boeing 787",color=discord.Colour.purple())
  embed.add_field(name="Basic Info",value="The Boeing 787 Dreamliner is an American wide-body jet airliner developed and manufactured by Boeing Commercial Airplanes. After dropping its Sonic Cruiser project, Boeing announced the conventional 7E7 on January 29, 2003, focused on efficiency. The program was launched on April 26, 2004, with an order for 50 from All Nippon Airways (ANA), targeting a 2008 introduction. On July 8, 2007, the prototype was rolled out without major systems and experienced multiple delays until its maiden flight on December 15, 2009.",inline=False)
  embed.add_field(name="Produced",value="2007-Present",inline=False)
  embed.add_field(name="Engines",value="General Electric GEnx",inline=False)
  embed.add_field(name="First Operator",value="All Nippon Airways",inline=False)
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/f/fc/Air_India%2C_VT-ANA%2C_Boeing_787-8_Dreamliner_%2840665210023%29.jpg")
  await ctx.send(embed=embed)
  

keep_alive()
  
client.run("OTYyNjc1MzM2OTIxODkwODU2.YlK_RQ.-CffKk03mj61MlAif0B2F2RohNg")

  
