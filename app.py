import streamlit as st

st.set_page_config(page_title="Factors of Production", page_icon="🏭", layout="wide")

st.title("🏭 Factors of Production")
st.write("A deep dive into the four resources every economy needs to produce goods and services: **Land, Labour, Capital, and Entrepreneurship.**")

st.divider()

topic = st.selectbox(
    "Choose a topic to explore in depth:",
    ["Overview", "Land", "Labour", "Capital", "Entrepreneurship", "How They Work Together", "Quiz Yourself"]
)

# ---------------------------------------------------------
if topic == "Overview":
    st.header("What Are Factors of Production?")
    st.write("""
Factors of production are the **inputs** used in the process of producing goods and services 
in order to make an economic profit. Every single product or service you've ever used — 
from a smartphone to a haircut — required some combination of these four resources.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("The Four Factors")
        st.markdown("""
        | Factor | Reward | Example |
        |---|---|---|
        | 🌍 Land | Rent | Farmland, oil, forests |
        | 👷 Labour | Wages | Workers, doctors, teachers |
        | 🏗️ Capital | Interest | Machines, tools, buildings |
        | 💡 Entrepreneurship | Profit | Business owners, risk-takers |
        """)

    with col2:
        st.subheader("Why This Matters")
        st.write("""
        Economists use this framework to understand:
        - How wealth is created in a society
        - Why some countries are richer than others
        - How income gets distributed (wages vs rent vs profit vs interest)
        - Why businesses succeed or fail based on how well they combine these inputs
        """)

    st.info("💡 **Key Insight:** No single factor can produce anything alone. A farmer (labour) needs land (soil) and a tractor (capital), and someone had to take the risk of starting the farm (entrepreneurship).")

# ---------------------------------------------------------
elif topic == "Land":
    st.header("🌍 Land")
    st.subheader("Definition")
    st.write("""
    In economics, "Land" refers to **all natural resources** that are used to produce goods and services — 
    not just the ground you walk on. This includes anything that exists in or on the Earth naturally, 
    without human effort creating it.
    """)

    st.subheader("What Counts as Land?")
    st.markdown("""
    - **Soil and terrain** — farmland, building plots, grazing land
    - **Water** — rivers, lakes, oceans (used for fishing, transport, hydroelectric power)
    - **Minerals** — iron ore, gold, coal, copper
    - **Forests** — timber, rubber, natural habitats
    - **Oil and natural gas** — fossil fuel reserves
    - **Climate and sunlight** — used in agriculture and solar energy
    - **Wildlife** — fish stocks, livestock grazing land
    """)

    st.subheader("Characteristics of Land")
    st.markdown("""
    1. **Fixed in supply** — Unlike labour or capital, the total amount of land on Earth cannot be increased. 
       You cannot manufacture more oil reserves or more square miles of continent.
    2. **Immobile (geographically)** — Land cannot be physically moved from one place to another. 
       A gold mine in South Africa cannot be relocated to Japan.
    3. **No cost of production** — Land is a "free gift of nature." Unlike a factory, nobody built the Amazon rainforest.
    4. **Heterogeneous** — Not all land is equal. Fertile farmland in Punjab is very different from 
       desert land in the Sahara.
    5. **Subject to the Law of Diminishing Returns** — Because land is fixed, adding more labour/capital 
       to the same plot eventually produces smaller and smaller increases in output.
    """)

    st.subheader("Reward for Land: Rent")
    st.write("""
    The payment made for the use of land is called **rent**. This isn't just house rent — economic rent 
    specifically refers to payment for the *natural* resource itself, separate from any buildings on it.
    """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A wheat farmer paying rent to use 10 acres of farmland
    - An oil company paying royalties to extract crude oil from land it leases
    - A solar power company using open desert land to install solar panels
    - A fishing company using ocean waters (a natural resource) to catch fish
    """)

    st.warning("⚠️ **Common Confusion:** In everyday language, we say we 'rent an apartment.' In economics, that payment is actually split — part is rent (for the land under the building) and part is return on capital (for the building itself).")

# ---------------------------------------------------------
elif topic == "Labour":
    st.header("👷 Labour")
    st.subheader("Definition")
    st.write("""
    Labour refers to the **physical and mental human effort** used in the production of goods and services. 
    It includes both blue-collar physical work and white-collar intellectual work.
    """)

    st.subheader("Types of Labour")
    st.markdown("""
    - **Skilled Labour** — requires training or education (doctors, engineers, software developers)
    - **Semi-skilled Labour** — requires some training (machine operators, drivers)
    - **Unskilled Labour** — requires little to no formal training (manual loading, basic farm work)
    - **Physical Labour** — bodily effort (construction workers, farmers)
    - **Mental Labour** — intellectual effort (writers, scientists, analysts)
    """)

    st.subheader("Characteristics of Labour")
    st.markdown("""
    1. **Labour is perishable** — A worker's time today cannot be stored and used tomorrow. 
       An hour of unused work capacity is lost forever.
    2. **Labour cannot be separated from the labourer** — Unlike a machine you can sell, 
       you cannot separate a worker's effort from the worker themselves.
    3. **Labour has poor bargaining power individually** — A single worker often has less negotiating 
       power than an employer, which is why trade unions exist.
    4. **Labour supply is influenced by population** — Birth rates, migration, retirement age, 
       and education levels all affect how much labour is available in an economy.
    5. **Efficiency varies** — Unlike a machine that performs identically each time, human productivity 
       is affected by motivation, health, working conditions, and skill.
    """)

    st.subheader("Reward for Labour: Wages")
    st.write("""
    Workers are paid **wages** (or salaries) in exchange for their labour. Wages can be:
    - **Time-based** — paid per hour, day, or month
    - **Piece-rate** — paid per unit of output produced
    - **Salary** — a fixed regular payment regardless of hours worked in a given day
    """)

    st.subheader("Factors Affecting Wage Levels")
    st.markdown("""
    - Level of skill and education required
    - Supply and demand for that type of labour
    - Risk involved in the job (hazard pay)
    - Location and cost of living
    - Bargaining power (unions, labour laws)
    """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A factory worker assembling cars (physical, semi-skilled labour)
    - A surgeon performing an operation (physical + highly skilled + mental labour)
    - A software engineer writing code (mental, skilled labour)
    - A farm labourer harvesting crops (physical, often unskilled labour)
    """)

# ---------------------------------------------------------
elif topic == "Capital":
    st.header("🏗️ Capital")
    st.subheader("Definition")
    st.write("""
    Capital refers to **man-made resources** used to produce other goods and services. 
    Unlike land, capital does NOT occur naturally — humans have to build it first.
    """)

    st.subheader("Types of Capital")
    st.markdown("""
    - **Fixed Capital** — long-lasting resources used repeatedly (machinery, buildings, tools, vehicles)
    - **Working Capital** — resources used up in a single production cycle (raw materials, fuel, cash for daily operations)
    - **Real Capital** — the physical/tangible tools and machines themselves
    - **Financial Capital** — money invested to acquire real capital (loans, shareholder investment)
    - **Human Capital** *(related but distinct)* — the skills, knowledge, and training embedded in workers, 
      which increases their productivity (this overlaps with Labour but is often discussed alongside Capital)
    """)

    st.subheader("Characteristics of Capital")
    st.markdown("""
    1. **Capital is man-made** — Unlike land, someone had to build/manufacture it. A tractor didn't exist 
       until humans designed and built one.
    2. **Capital depreciates** — Machines wear out over time and need replacement or maintenance.
    3. **Capital is mobile** — Unlike land, a machine can usually be transported from one location to another.
    4. **Capital increases productivity** — A farmer with a tractor can till far more land per day 
       than one with only hand tools.
    5. **Capital requires initial investment (saving)** — Someone must forgo current consumption 
       to fund the creation of capital goods.
    """)

    st.subheader("Reward for Capital: Interest")
    st.write("""
    The payment made for the use of capital is called **interest**. When someone lends money to a business 
    so it can buy machinery, they are compensated with interest for giving up the use of their money.
    """)

    st.subheader("Capital vs. Money — An Important Distinction")
    st.write("""
    In everyday language, people often say "I need more capital" meaning "I need more money." 
    But in economics, **money itself is not capital** — money is only capital *when it is used to 
    purchase capital goods* like machinery or equipment. Money sitting idle in a wallet is not a factor of production.
    """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A tractor used on a farm (fixed capital)
    - A factory building and its assembly line machines (fixed capital)
    - Raw cotton bought to make into cloth (working capital)
    - A delivery truck used by a logistics company (fixed capital)
    - A laptop used by a graphic designer (fixed capital)
    """)

# ---------------------------------------------------------
elif topic == "Entrepreneurship":
    st.header("💡 Entrepreneurship")
    st.subheader("Definition")
    st.write("""
    Entrepreneurship is the **skill and initiative** of organizing the other three factors of production 
    (Land, Labour, Capital) to produce goods and services, while taking on the **risk** of the business venture.
    """)

    st.subheader("Key Functions of an Entrepreneur")
    st.markdown("""
    1. **Organizing** — Bringing together land, labour, and capital in the right combination
    2. **Risk-bearing** — Investing money and time without a guarantee of success or profit
    3. **Innovation** — Introducing new products, processes, or ways of doing business
    4. **Decision-making** — Deciding what to produce, how much, and for whom
    5. **Leadership** — Directing and motivating the workforce toward a shared goal
    """)

    st.subheader("Characteristics of an Entrepreneur")
    st.markdown("""
    - **Risk-taker** — willing to invest resources without guaranteed returns
    - **Innovative** — finds new ways to solve problems or meet needs
    - **Decisive** — makes choices quickly under uncertainty
    - **Resilient** — able to handle failure and try again
    - **Visionary** — can identify opportunities others might miss
    """)

    st.subheader("Reward for Entrepreneurship: Profit")
    st.write("""
    Unlike the other three factors, entrepreneurship does not have a guaranteed reward. 
    - If the business succeeds, the entrepreneur earns **profit**.
    - If the business fails, the entrepreneur may face a **loss** — this is what separates 
      entrepreneurship's reward from wages, rent, and interest, which are typically guaranteed by contract.
    """)

    st.subheader("Why Entrepreneurship Is Considered a Special Factor")
    st.markdown("""
    - It is the only factor that bears **uninsurable risk**
    - It is the **organizing** factor — without it, land, labour, and capital would simply sit idle
    - Its reward (profit) is a **residual** — what's left after paying rent, wages, and interest, 
      which is why profit can be negative (a loss) unlike the other three rewards
    """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A person starting a bakery — combining flour (raw material/working capital), 
      an oven (capital), bakers (labour), and a shop location (land)
    - A tech founder building a startup — combining coders (labour), 
      office space and servers (capital), and investor funding
    - A farmer who decides to start their own organic vegetable business rather than just working for someone else
    """)

# ---------------------------------------------------------
elif topic == "How They Work Together":
    st.header("🔗 How the Four Factors Work Together")
    st.write("""
    None of the four factors can produce anything in isolation. Let's trace through one complete 
    example to see how they combine.
    """)

    st.subheader("Example: Starting a Small Bakery")
    st.markdown("""
    | Factor | Role in the Bakery |
    |---|---|
    | 🌍 **Land** | The plot of land or shop space where the bakery is built |
    | 👷 **Labour** | The bakers who mix, knead, and bake the bread |
    | 🏗️ **Capital** | The oven, mixing machines, delivery van, and the flour bought to bake with |
    | 💡 **Entrepreneurship** | The person who had the idea, took a loan, hired the bakers, and bears the risk if it fails |
    """)

    st.write("""
    If the bakery succeeds and makes money, here's how the income gets distributed:
    - The **landlord** receives **rent** for the shop space
    - The **bakers** receive **wages** for their work
    - The **bank** that lent money for the oven receives **interest**
    - The **entrepreneur** keeps whatever is left over as **profit**

    If the bakery fails, the landlord, bakers, and bank may still need to be paid (depending on contracts), 
    but the entrepreneur absorbs the **loss** — this is the defining risk of entrepreneurship.
    """)

    st.subheader("A Second Example: A Software Startup")
    st.markdown("""
    | Factor | Role in the Startup |
    |---|---|
    | 🌍 **Land** | The office space (or even just the physical space of a server farm/data center) |
    | 👷 **Labour** | The software engineers, designers, and support staff |
    | 🏗️ **Capital** | Laptops, servers, cloud computing infrastructure |
    | 💡 **Entrepreneurship** | The founder(s) who identified the problem, raised funding, and lead the company |
    """)

    st.success("✅ **Big Takeaway:** Production always requires all four factors working in combination. The efficiency with which an economy combines these factors largely determines its overall wealth and productivity.")

# ---------------------------------------------------------
elif topic == "Quiz Yourself":
    st.header("📝 Quick Quiz")
    st.write("Test your understanding! Select an answer for each question.")

    q1 = st.radio(
        "1. What is the reward for Land?",
        ["Wages", "Rent", "Interest", "Profit"],
        index=None
    )
    if q1:
        st.write("✅ Correct!" if q1 == "Rent" else "❌ Not quite — the reward for Land is **Rent**.")

    q2 = st.radio(
        "2. Which factor bears the risk of loss?",
        ["Land", "Labour", "Capital", "Entrepreneurship"],
        index=None
    )
    if q2:
        st.write("✅ Correct!" if q2 == "Entrepreneurship" else "❌ Not quite — **Entrepreneurship** is the risk-bearing factor.")

    q3 = st.radio(
        "3. Is money itself considered Capital in economics?",
        ["Yes, always", "No, only when used to buy capital goods", "No, money is never capital"],
        index=None
    )
    if q3:
        st.write("✅ Correct!" if q3 == "No, only when used to buy capital goods" else "❌ Not quite — money is only capital when it's used to purchase capital goods like machinery.")

    q4 = st.radio(
        "4. Which factor is geographically immobile?",
        ["Land", "Labour", "Capital", "Entrepreneurship"],
        index=None
    )
    if q4:
        st.write("✅ Correct!" if q4 == "Land" else "❌ Not quite — **Land** cannot be physically relocated.")

st.divider()
st.caption("Built to explain the Factors of Production: Land, Labour, Capital, and Entrepreneurship.")
