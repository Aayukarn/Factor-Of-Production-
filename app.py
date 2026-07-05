import streamlit as st

st.set_page_config(page_title="Factors of Production", page_icon="🏭", layout="wide")

st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .hero-banner {
        background: linear-gradient(135deg, #2d5f4c 0%, #4a7c6d 25%, #d97b3f 50%, #3a6ea5 75%, #6b4c8a 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }
    .hero-banner h1 {
        color: white;
        font-size: 2.6rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }
    .hero-banner p {
        color: rgba(255,255,255,0.92);
        font-size: 1.1rem;
        margin-top: 0.6rem;
        margin-bottom: 0;
    }
    .hero-credit {
        color: rgba(255,255,255,0.88);
        font-size: 0.95rem;
        margin: 0.25rem 0 0 0;
        letter-spacing: 0.3px;
    }
    .hero-credit.school {
        font-weight: 700;
        font-size: 1rem;
    }
    .factor-pill-row {
        display: flex;
        gap: 0.6rem;
        margin-top: 1.2rem;
        flex-wrap: wrap;
    }
    .factor-pill {
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(4px);
        color: white;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.35);
    }
    h2, h3 {
        color: #26332d;
        font-weight: 700;
    }
    .stSelectbox label {
        font-size: 1.05rem;
        font-weight: 600;
        color: #26332d;
    }
    div[data-baseweb="select"] > div {
        border-radius: 10px;
        border: 2px solid #4a7c6d;
    }
    .stAlert {
        border-radius: 12px;
    }
    img {
        border-radius: 12px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
    <h1>🏭 Factors of Production</h1>
    <p class="hero-credit school">BY KAMAL MODEL SR SEC SCHOOL</p>
    <p class="hero-credit"><strong>SPECIAL THANKS TO AAYU KARN AND KUNAL KUMAR MAHTO THE MAKER OF THIS WEBSITE</strong></p>
    <div class="factor-pill-row">
        <span class="factor-pill">🌍 Land</span>
        <span class="factor-pill">👷 Labour</span>
        <span class="factor-pill">🏗️ Capital</span>
        <span class="factor-pill">💡 Entrepreneurship</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

topic = st.selectbox(
    "Choose a topic to explore in depth:",
    ["Overview", "Land", "Labour", "Capital", "Entrepreneurship",
     "Economic Theories & Thinkers", "How They Work Together",
     "Country Case Studies", "Modern Debates", "Quiz Yourself"]
)

# ---------------------------------------------------------
if topic == "Overview":
    st.header("What Are Factors of Production?")
    st.write("""
Factors of production are the **inputs** used in the process of producing goods and services 
in order to make an economic profit. Every product or service ever made — from a smartphone 
to a haircut — required some combination of these four resources. This concept sits at the very 
foundation of economics, because it answers the most basic question any society must solve: 
**how do we take limited resources and turn them into the things people need and want?**
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
        - How economic growth happens over time (adding more/better factors, or combining them more efficiently)
        """)

    st.info("💡 **Key Insight:** No single factor can produce anything alone. A farmer (labour) needs land (soil) and a tractor (capital), and someone had to take the risk of starting the farm (entrepreneurship).")

    st.subheader("A Brief History of the Concept")
    st.write("""
    The idea that production requires distinct categories of inputs goes back centuries:
    - **Physiocrats (18th century France)**, led by François Quesnay, believed *land* was the only true source of wealth, 
      since agriculture was seen as the only activity that produced a genuine surplus.
    - **Adam Smith (1776)**, in *The Wealth of Nations*, identified **Land, Labour, and Capital** as the three 
      classical factors, and connected each to a form of income: rent, wages, and profit.
    - **David Ricardo** and other classical economists refined the theory of rent and diminishing returns on land.
    - **Jean-Baptiste Say (early 1800s)** is widely credited with identifying **Entrepreneurship** as a distinct 
      fourth factor, recognizing the entrepreneur's unique role in combining resources and bearing risk.
    - **Alfred Marshall (late 1800s)** helped formalize the modern four-factor model still taught today, 
      linking each factor cleanly to its corresponding reward (rent, wages, interest, profit).
    """)

    st.subheader("The Basic Economic Problem")
    st.write("""
    All of economics exists because of one core issue: **resources are scarce, but human wants are unlimited.** 
    The factors of production are how societies try to solve this problem — every economic system 
    (capitalism, socialism, mixed economies) is essentially a different answer to the question: 
    *"Who owns and controls land, labour, capital, and entrepreneurship, and how should the rewards be shared?"*
    """)

# ---------------------------------------------------------
elif topic == "Land":
    st.header("🌍 Land")

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Definition")
        st.write("""
        In economics, "Land" refers to **all natural resources** that are used to produce goods and services — 
        not just the ground you walk on. This includes anything that exists in or on the Earth naturally, 
        without human effort creating it. Economists sometimes call this the **"free gift of nature."**
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=400", caption="Farmland")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=400", caption="Forests")
    with col_text:
        st.subheader("What Counts as Land?")
        st.markdown("""
        - **Soil and terrain** — farmland, building plots, grazing land
        - **Water** — rivers, lakes, oceans (used for fishing, transport, hydroelectric power)
        - **Minerals** — iron ore, gold, coal, copper, lithium, rare earth metals
        - **Forests** — timber, rubber, natural habitats
        - **Oil and natural gas** — fossil fuel reserves
        - **Climate and sunlight** — used in agriculture and solar energy generation
        - **Wildlife and fish stocks** — natural populations harvested for food or materials
        - **The electromagnetic spectrum** — a modern example; radio frequencies are a genuinely 
          scarce natural resource that governments auction off to telecom companies
        """)

    st.subheader("Characteristics of Land")
    st.markdown("""
    1. **Fixed in supply** — Unlike labour or capital, the total amount of land on Earth cannot be increased. 
       You cannot manufacture more oil reserves or more square miles of continent (with rare exceptions 
       like land reclamation, e.g. Netherlands' polders or Singapore's land reclamation projects, 
       which are extremely costly and limited).
    2. **Immobile (geographically)** — Land cannot be physically moved from one place to another. 
       A gold mine in South Africa cannot be relocated to Japan.
    3. **No cost of production** — Land is a "free gift of nature." Unlike a factory, nobody built the Amazon rainforest.
    4. **Heterogeneous** — Not all land is equal. Fertile farmland in Punjab is very different from 
       desert land in the Sahara; a coastal plot suited to a port is different from a mountain suited to skiing.
    5. **Subject to the Law of Diminishing Returns** — Because land is fixed, adding more labour/capital 
       to the same plot eventually produces smaller and smaller increases in output (this is called 
       **diminishing marginal returns**, first formally analyzed by David Ricardo).
    6. **Original and indestructible powers of the soil** — a classical phrase (from Ricardo) referring to land's 
       basic fertility, which exists independent of any human investment in it.
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Reward for Land: Rent")
        st.write("""
        The payment made for the use of land is called **rent**. This isn't just house rent — economic rent 
        specifically refers to payment for the *natural* resource itself, separate from any buildings on it.

        **Ricardian Theory of Rent:** David Ricardo argued that rent arises because land differs in fertility/location. 
        As population grows and less fertile land is brought into cultivation, the *most fertile* land earns a 
        premium (rent) simply because it produces more for the same effort. In his model, rent is a 
        **surplus** — it doesn't need to exist for production to happen; it exists because good land is scarce 
        relative to demand.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1518623489648-a173ef7824f3?w=400", caption="Minerals & Mining")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1439405326854-014607f694d7?w=400", caption="Oceans & Water")
    with col_text:
        st.subheader("Land Degradation & Sustainability")
        st.write("""
        Because land is fixed and mostly non-renewable on human timescales, its **overuse** is a major global concern:
        - **Deforestation** reduces usable forest land and disrupts climate regulation
        - **Soil erosion and desertification** — the UN estimates a significant share of the world's land is already degraded, 
          threatening future agricultural productivity
        - **Overfishing** depletes a "renewable" resource faster than it can regenerate
        - **Climate change** is altering which land is even viable for agriculture, shifting growing zones toward the poles

        This raises the modern economic question of **sustainable resource use** — how to use land productively today 
        without destroying its productive capacity for future generations.
        """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A wheat farmer paying rent to use 10 acres of farmland
    - An oil company paying royalties to extract crude oil from land it leases
    - A solar power company using open desert land to install solar panels
    - A fishing company using ocean waters (a natural resource) to catch fish
    - A telecom company paying the government for spectrum rights (a modern "natural resource")
    - Saudi Arabia's economy historically built almost entirely around oil (a land-based natural resource)
    """)

    st.warning("⚠️ **Common Confusion:** In everyday language, we say we 'rent an apartment.' In economics, that payment is actually split — part is rent (for the land under the building) and part is return on capital (for the building itself).")

# ---------------------------------------------------------
elif topic == "Labour":
    st.header("👷 Labour")

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Definition")
        st.write("""
        Labour refers to the **physical and mental human effort** used in the production of goods and services. 
        It includes both blue-collar physical work and white-collar intellectual work — and is the only factor 
        that is inseparable from a living, thinking human being.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1521791136064-7986c2920216?w=400", caption="Factory Workers")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400", caption="Surgeon (Skilled Labour)")
    with col_text:
        st.subheader("Types of Labour")
        st.markdown("""
        - **Skilled Labour** — requires training or education (doctors, engineers, software developers)
        - **Semi-skilled Labour** — requires some training (machine operators, drivers)
        - **Unskilled Labour** — requires little to no formal training (manual loading, basic farm work)
        - **Physical Labour** — bodily effort (construction workers, farmers)
        - **Mental Labour** — intellectual effort (writers, scientists, analysts)
        - **Casual Labour** — irregular, often daily-wage work with no long-term contract
        - **Migrant Labour** — workers who move (domestically or internationally) to find work opportunities
        """)

    st.subheader("Characteristics of Labour")
    st.markdown("""
    1. **Labour is perishable** — A worker's time today cannot be stored and used tomorrow. 
       An hour of unused work capacity is lost forever, unlike a raw material that can sit in a warehouse.
    2. **Labour cannot be separated from the labourer** — Unlike a machine you can sell, 
       you cannot separate a worker's effort from the worker themselves; this is why working conditions, 
       dignity, and rights are central labour issues in a way they aren't for capital goods.
    3. **Labour has poor bargaining power individually** — A single worker often has less negotiating 
       power than an employer, which is why trade unions and collective bargaining exist.
    4. **Labour supply is influenced by population** — Birth rates, migration, retirement age, 
       and education levels all affect how much labour is available in an economy over time.
    5. **Efficiency varies** — Unlike a machine that performs identically each time, human productivity 
       is affected by motivation, health, working conditions, nutrition, and skill — this is why 
       "efficiency wages" (paying above-market wages to boost morale and productivity) is a real strategy firms use.
    6. **Labour is mobile, but imperfectly** — Workers can move between jobs/regions, but language, 
       family ties, visa restrictions, and licensing rules limit this mobility compared to how easily money moves.
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Reward for Labour: Wages")
        st.write("""
        Workers are paid **wages** (or salaries) in exchange for their labour. Wages can be structured as:
        - **Time-based** — paid per hour, day, or month
        - **Piece-rate** — paid per unit of output produced
        - **Salary** — a fixed regular payment regardless of hours worked in a given day
        - **Commission-based** — tied to sales or performance outcomes
        - **Real wages vs Nominal wages** — nominal wage is the money amount received; real wage adjusts 
          for inflation to show actual purchasing power, which is the figure economists care about most
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400", caption="Software Engineer")

    st.subheader("Factors Affecting Wage Levels")
    st.markdown("""
    - Level of skill and education required (human capital)
    - Supply and demand for that type of labour in the market
    - Risk involved in the job (hazard pay for dangerous work like mining or deep-sea fishing)
    - Location and cost of living
    - Bargaining power (unions, minimum wage laws, labour regulations)
    - Productivity — in competitive markets, wages tend to reflect the **marginal productivity** of labour 
      (the extra output produced by one more worker)
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=400", caption="Farm Labour")
    with col_text:
        st.subheader("Division of Labour & Specialization")
        st.write("""
        Adam Smith's famous **pin factory example** showed that breaking production into specialized tasks 
        massively increases output — ten workers each doing one small step in making a pin could produce 
        thousands of times more pins per day than ten workers each making a whole pin individually. 
        This principle of **specialization** underlies almost all modern industry, global trade, and 
        even careers themselves (people specializing in one profession rather than being generalists).
        """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A factory worker assembling cars (physical, semi-skilled labour)
    - A surgeon performing an operation (physical + highly skilled + mental labour)
    - A software engineer writing code (mental, skilled labour)
    - A farm labourer harvesting crops (physical, often unskilled labour)
    - A gig-economy delivery rider (physical, casual, flexible labour)
    - Garment workers in Bangladesh's textile industry, a major source of national export income
    """)

# ---------------------------------------------------------
elif topic == "Capital":
    st.header("🏗️ Capital")

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Definition")
        st.write("""
        Capital refers to **man-made resources** used to produce other goods and services. 
        Unlike land, capital does NOT occur naturally — humans have to build it first, using land, 
        labour, and existing capital in a continuous cycle.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=400", caption="Industrial Machinery")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1595656180594-2fa9b3d0aa30?w=400", caption="Tractor (Fixed Capital)")
    with col_text:
        st.subheader("Types of Capital")
        st.markdown("""
        - **Fixed Capital** — long-lasting resources used repeatedly over many production cycles 
          (machinery, buildings, tools, vehicles)
        - **Working Capital** — resources used up in a single production cycle (raw materials, fuel, 
          cash for daily operations)
        - **Real Capital** — the physical/tangible tools and machines themselves
        - **Financial Capital** — money invested to acquire real capital (loans, shareholder investment, venture capital)
        - **Human Capital** *(related but distinct)* — the skills, knowledge, training, and health embedded 
          in workers, which increases their productivity; economists like Gary Becker argued education and 
          training should be thought of as an *investment* in capital, not just a cost
        - **Social/Infrastructure Capital** — roads, ports, electricity grids, the internet — often built 
          by governments and used by all businesses in an economy
        - **Intellectual Capital** — patents, trademarks, brand value, proprietary software and algorithms
        """)

    st.subheader("Characteristics of Capital")
    st.markdown("""
    1. **Capital is man-made** — Unlike land, someone had to build/manufacture it. A tractor didn't exist 
       until humans designed and built one.
    2. **Capital depreciates** — Machines wear out over time and need replacement or maintenance; 
       businesses account for this with "depreciation" in their financial statements.
    3. **Capital is mobile** — Unlike land, a machine can usually be transported from one location to another, 
       and financial capital can move across borders almost instantly.
    4. **Capital increases productivity** — A farmer with a tractor can till far more land per day 
       than one with only hand tools; this is called **capital deepening**.
    5. **Capital requires initial investment (saving)** — Someone must forgo current consumption 
       to fund the creation of capital goods — this is why national **savings rates** matter enormously 
       for long-term economic growth.
    6. **Capital is subject to obsolescence** — beyond physical wear, capital can become outdated 
       due to new technology (e.g., a factory built for older machinery may become economically obsolete 
       even if physically functional).
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Reward for Capital: Interest")
        st.write("""
        The payment made for the use of capital is called **interest**. When someone lends money to a business 
        so it can buy machinery, they are compensated with interest for giving up the use of their money 
        and for the risk that it might not be repaid.

        **Time preference theory** explains why interest exists at all: people generally prefer having money 
        *now* rather than later (a concept called "time preference"), so lenders must be compensated with 
        interest to convince them to delay their own consumption.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1565043589221-1a6fd9ae45c7?w=400", caption="Factory Assembly Line")

    st.subheader("Capital vs. Money — An Important Distinction")
    st.write("""
    In everyday language, people often say "I need more capital" meaning "I need more money." 
    But in economics, **money itself is not capital** — money is only capital *when it is used to 
    purchase capital goods* like machinery or equipment. Money sitting idle in a wallet is not a 
    factor of production; it only becomes productive capital once it's converted into a tool, 
    machine, or building that helps produce something.
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Laptop (Digital Capital)")
    with col_text:
        st.subheader("Capital Formation and Economic Growth")
        st.write("""
        **Gross Capital Formation** (also called investment) is one of the four components of GDP, alongside 
        consumption, government spending, and net exports. Countries with high rates of capital formation 
        (building more factories, infrastructure, and machinery) tend to see faster long-term economic growth — 
        this is a core insight of the **Solow Growth Model**, a foundational framework in growth economics.
        """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A tractor used on a farm (fixed capital)
    - A factory building and its assembly line machines (fixed capital)
    - Raw cotton bought to make into cloth (working capital)
    - A delivery truck used by a logistics company (fixed capital)
    - A laptop used by a graphic designer (fixed capital)
    - A country's national highway network (infrastructure capital)
    - A tech company's patented algorithm (intellectual capital)
    """)

# ---------------------------------------------------------
elif topic == "Entrepreneurship":
    st.header("💡 Entrepreneurship")

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Definition")
        st.write("""
        Entrepreneurship is the **skill and initiative** of organizing the other three factors of production 
        (Land, Labour, Capital) to produce goods and services, while taking on the **risk** of the business venture. 
        It is often called the "fourth factor" because it was added to the classical three (land, labour, capital) 
        later in the development of economic theory. Unlike a machine or a plot of land, entrepreneurship is 
        not a "thing" — it is a **capability**: the ability to spot an opportunity, gather the other three 
        factors around it, and commit to acting before anyone can be certain it will work.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=400", caption="Founder at Work")

    st.subheader("Key Functions of an Entrepreneur")
    st.markdown("""
    1. **Organizing** — Bringing together land, labour, and capital in the right combination and proportion
    2. **Risk-bearing** — Investing money and time without a guarantee of success or profit
    3. **Innovation** — Introducing new products, processes, or ways of doing business 
       (economist Joseph Schumpeter called this "creative destruction")
    4. **Decision-making** — Deciding what to produce, how much, for whom, and at what price
    5. **Leadership** — Directing and motivating the workforce toward a shared goal
    6. **Uncertainty-bearing** — Economist Frank Knight distinguished between measurable "risk" 
       (which can be insured against) and true "uncertainty" (which cannot) — arguing entrepreneurial 
       profit is specifically the reward for bearing this uninsurable uncertainty
    7. **Coordination across time** — An entrepreneur commits resources today for an outcome that will 
       only be known months or years later, effectively betting on their own judgment about the future
    8. **Market discovery** — Economist Israel Kirzner described entrepreneurship as "alertness" — 
       noticing profit opportunities that already exist in the market but that nobody else has spotted yet, 
       such as a price gap between two markets, or an unmet need customers haven't been able to articulate
    """)

    st.subheader("Characteristics of an Entrepreneur")
    st.markdown("""
    - **Risk-taker** — willing to invest resources without guaranteed returns
    - **Innovative** — finds new ways to solve problems or meet needs
    - **Decisive** — makes choices quickly under uncertainty
    - **Resilient** — able to handle failure and try again (most successful entrepreneurs have failed at least once)
    - **Visionary** — can identify opportunities others might miss
    - **Resourceful** — able to do more with limited land, labour, and capital than competitors
    - **Self-motivated** — often works without external supervision or a guaranteed paycheck
    - **Comfortable with ambiguity** — able to make decisions with incomplete information
    - **Adaptive** — willing to change the original plan based on real feedback ("pivoting")
    """)

    st.subheader("Reward for Entrepreneurship: Profit")
    st.write("""
    Unlike the other three factors, entrepreneurship does not have a guaranteed reward. 
    - If the business succeeds, the entrepreneur earns **profit**.
    - If the business fails, the entrepreneur may face a **loss** — this is what separates 
      entrepreneurship's reward from wages, rent, and interest, which are typically guaranteed by contract 
      (a landlord gets rent whether the business succeeds or not; wages are typically owed regardless of profit).

    **Normal profit vs. Economic (Supernormal) profit** — a distinction worth knowing at a competition level:
    - **Normal profit** is the *minimum* return needed to keep an entrepreneur in a particular business rather 
      than switching to their next-best alternative. It's technically treated as a cost, not a true reward.
    - **Economic profit** (also called supernormal or abnormal profit) is anything earned *above* normal 
      profit — this is the genuine reward for entrepreneurship, usually arising from innovation, 
      first-mover advantage, or a temporary monopoly position before competitors catch up.
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=400", caption="Startup Team")
    with col_text:
        st.subheader("Types of Entrepreneurship")
        st.markdown("""
        - **Small Business Entrepreneurship** — local shops, restaurants, freelancers; the most common type globally, 
          typically funded through personal savings, family, or small bank loans
        - **Scalable Startup Entrepreneurship** — ventures explicitly built to grow fast and large, often funded by 
          venture capital (e.g., tech startups aiming to become billion-dollar "unicorns")
        - **Social Entrepreneurship** — ventures where the primary goal is solving a social or environmental 
          problem, with profit as a secondary or supporting goal (e.g., a company selling affordable solar 
          lamps in areas without reliable electricity)
        - **Intrapreneurship** — entrepreneurial behavior *within* an existing large company, where an employee 
          is given resources and freedom to build a new product or division as if it were their own startup
        - **Serial Entrepreneurship** — individuals who start, grow, and often exit multiple businesses over 
          their career rather than running just one
        - **Necessity Entrepreneurship vs. Opportunity Entrepreneurship** — a key distinction in development 
          economics: *necessity* entrepreneurs start a business because they have no better employment option 
          (common in developing economies), while *opportunity* entrepreneurs start a business specifically 
          because they've identified a promising market gap
        """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Schumpeter's Theory of the Entrepreneur")
        st.write("""
        Economist **Joseph Schumpeter** (early-to-mid 1900s) argued entrepreneurs are the engine of 
        economic progress through **"creative destruction"** — the process by which new innovations 
        make old products, companies, and industries obsolete, while creating entirely new markets. 
        Examples: the automobile destroying the horse-carriage industry; streaming destroying the DVD rental industry; 
        smartphones destroying the standalone camera and MP3 player industries.

        Schumpeter identified **five types of innovation** an entrepreneur can introduce:
        1. A new good (or a new quality of an existing good)
        2. A new method of production
        3. A new market (opening a market that didn't exist for that region/product before)
        4. A new source of supply of raw materials
        5. A new organizational structure for an industry (e.g., creating or breaking up a monopoly)
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1556761175-b413da4baf72?w=400", caption="Pitching an Idea")

    st.subheader("Kirzner's Theory of Alertness")
    st.write("""
    Economist **Israel Kirzner** offered a contrasting view to Schumpeter: rather than entrepreneurs 
    *creating* disruption, Kirzner argued their key skill is **alertness** to opportunities that already 
    exist but are unnoticed — for instance, spotting that a product sells for less in one market than 
    another and profiting from that gap (arbitrage), or noticing an underserved customer need. In this 
    view, entrepreneurship is fundamentally about *discovery*, while Schumpeter's view emphasizes *disruption*.
    """)

    st.subheader("Why Entrepreneurship Is Considered a Special Factor")
    st.markdown("""
    - It is the only factor that bears **uninsurable risk**
    - It is the **organizing** factor — without it, land, labour, and capital would simply sit idle
    - Its reward (profit) is a **residual** — what's left after paying rent, wages, and interest, 
      which is why profit can be negative (a loss) unlike the other three rewards
    - It drives **innovation and economic dynamism**, not just static production
    - It is the hardest factor to measure or quantify — you can count acres of land or hours of labour, 
      but there's no direct unit for "amount of entrepreneurship"
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400", caption="Small Business Owner")
    with col_text:
        st.subheader("The Entrepreneurial Ecosystem")
        st.write("""
        Modern economists increasingly study entrepreneurship not just as an individual trait but as something 
        shaped by the surrounding **ecosystem**, including:
        - **Access to capital** — availability of venture capital, angel investors, or business loans
        - **Regulatory environment** — how easy or costly it is to legally register and run a business
        - **Education and culture** — whether risk-taking and failure are socially encouraged or stigmatized
        - **Infrastructure** — reliable internet, transport, and utilities lowering the cost of starting up
        - **Mentorship and networks** — incubators, accelerators, and university programs that support new founders

        This is why entrepreneurship hubs like Silicon Valley, Bangalore, or Tel Aviv develop — they combine 
        many of these supporting conditions in one place, creating a self-reinforcing cycle of new ventures.
        """)

    st.subheader("Global Entrepreneurship Snapshot")
    st.write("""
    Organizations like the **Global Entrepreneurship Monitor (GEM)** and the World Bank's 
    **Doing Business** reports track entrepreneurship activity worldwide, generally finding that:
    - Many developing economies have very **high rates of necessity-driven entrepreneurship**, 
      since formal employment opportunities are limited
    - Advanced economies tend to have more **opportunity-driven and scalable** entrepreneurship, 
      supported by deeper capital markets and stronger legal protections for business owners
    - Countries that reduce the time and cost to legally register a new business tend to see 
      measurably higher rates of formal entrepreneurship (versus informal, unregistered business activity)
    """)

    st.subheader("Real World Examples")
    st.markdown("""
    - A person starting a bakery — combining flour (raw material/working capital), 
      an oven (capital), bakers (labour), and a shop location (land)
    - A tech founder building a startup — combining coders (labour), 
      office space and servers (capital), and investor funding
    - A farmer who decides to start their own organic vegetable business rather than just working for someone else
    - Historical examples: Henry Ford reorganizing car manufacturing with the assembly line; 
      Ray Kroc scaling McDonald's into a franchise model
    - **Social entrepreneurship example:** Muhammad Yunus and the Grameen Bank, which pioneered 
      microfinance — small loans to entrepreneurs too poor to qualify for traditional bank credit
    - **Intrapreneurship example:** An employee inside a large tech company pitching and being given 
      a small team and budget to build an entirely new product line
    - **Necessity entrepreneurship example:** A street vendor in an economy with high unemployment, 
      starting an informal food stall because formal jobs are scarce
    """)

# ---------------------------------------------------------
elif topic == "Economic Theories & Thinkers":
    st.header("📚 Key Economic Theories & Thinkers")
    st.write("""
    The four-factor model didn't appear overnight — it developed over roughly 250 years of economic thought. 
    Here are the major contributors and how their ideas connect to what you've learned.
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Adam Smith (1723–1790)")
        st.write("""
        Often called the "father of modern economics," Smith's 1776 book *The Wealth of Nations* first 
        systematically linked the three original factors (land, labour, capital) to their respective 
        incomes (rent, wages, profit). He also introduced the idea of the **"invisible hand"** — the concept 
        that individuals pursuing their own self-interest in a free market can unintentionally benefit society as a whole.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=400", caption="Classical Economics Era")

    st.subheader("David Ricardo (1772–1823)")
    st.write("""
    Best known for his **theory of rent**, explaining why landowners earn rent even though land itself 
    has no cost of production — because fertile land is scarce relative to demand. He also developed 
    the theory of **comparative advantage**, explaining why countries benefit from trading even if 
    one country is better at producing everything.
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400", caption="Economic Theory & Books")
    with col_text:
        st.subheader("Jean-Baptiste Say (1767–1832)")
        st.write("""
        A French economist credited with identifying **entrepreneurship** as a distinct factor of production, 
        separate from simple "labour management." He emphasized the entrepreneur's role in shifting resources 
        from lower-value to higher-value uses.
        """)

    st.subheader("Karl Marx (1818–1883)")
    st.write("""
    Offered a critical view of the factors of production, particularly focused on **labour**. Marx argued 
    that workers create more value than they are paid in wages (which he called "surplus value"), 
    and that this surplus is captured by capital owners as profit — forming the basis of his critique 
    of capitalism and his labour theory of value.
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("Alfred Marshall (1842–1924)")
        st.write("""
        Helped formalize the modern **marginalist** approach to economics, including the idea that each 
        factor of production is paid according to its **marginal productivity** — the additional output 
        generated by one more unit of that factor. This is the dominant framework used in modern economics today.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=400", caption="Markets & Trade")

    st.subheader("Joseph Schumpeter (1883–1950)")
    st.write("""
    Elevated the importance of the entrepreneur through his theory of **"creative destruction"** — 
    arguing that innovation-driven entrepreneurship, not just efficient use of existing resources, 
    is the true engine of long-term economic growth and capitalism's defining feature.
    """)

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1543286386-713bdd548da4?w=400", caption="Industrial Progress")
    with col_text:
        st.subheader("Frank Knight (1885–1972)")
        st.write("""
        Distinguished between **risk** (measurable, insurable probability of loss) and **uncertainty** 
        (unmeasurable, uninsurable unknowns). Knight argued entrepreneurial profit is specifically the 
        reward for bearing this second, uninsurable kind of uncertainty — a foundational idea in modern 
        theories of the firm and entrepreneurship.
        """)

    st.subheader("Robert Solow (1924–2023)")
    st.write("""
    Developed the **Solow Growth Model**, showing mathematically how capital accumulation, labour force 
    growth, and technological progress combine to drive long-term economic growth — and importantly, 
    that technology/innovation (closely tied to entrepreneurship) is the factor that allows growth to 
    continue indefinitely, since simply adding more capital alone runs into diminishing returns.
    """)

# ---------------------------------------------------------
elif topic == "How They Work Together":
    st.header("🔗 How the Four Factors Work Together")
    st.write("""
    None of the four factors can produce anything in isolation. Let's trace through complete 
    examples to see how they combine in practice.
    """)

    st.subheader("Example 1: Starting a Small Bakery")
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

    st.subheader("Example 2: A Software Startup")
    st.markdown("""
    | Factor | Role in the Startup |
    |---|---|
    | 🌍 **Land** | The office space (or even just the physical space of a server farm/data center) |
    | 👷 **Labour** | The software engineers, designers, and support staff |
    | 🏗️ **Capital** | Laptops, servers, cloud computing infrastructure |
    | 💡 **Entrepreneurship** | The founder(s) who identified the problem, raised funding, and lead the company |
    """)

    st.subheader("Example 3: A National Automobile Industry")
    st.markdown("""
    | Factor | Role in the Auto Industry |
    |---|---|
    | 🌍 **Land** | Iron ore and rubber-producing regions; land the factory is built on |
    | 👷 **Labour** | Assembly line workers, engineers, designers, sales staff |
    | 🏗️ **Capital** | Robotic assembly lines, factory buildings, R&D equipment |
    | 💡 **Entrepreneurship** | The company's founders and leadership deciding what cars to build and how to compete |
    """)

    st.write("""
    Scaling this up to a national level: a country's total production (its **GDP**) is essentially 
    the sum of millions of these combinations happening simultaneously across every industry.
    """)

    st.success("✅ **Big Takeaway:** Production always requires all four factors working in combination. The efficiency with which an economy combines these factors — and how fairly it distributes the rewards — largely determines its overall wealth, growth rate, and standard of living.")

# ---------------------------------------------------------
elif topic == "Country Case Studies":
    st.header("🌐 Country Case Studies")
    st.write("""
    Different countries have built their economies by emphasizing different factors of production. 
    These examples show how the four-factor framework plays out at a national scale.
    """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("🇸🇦 Saudi Arabia — Land-Driven Economy")
        st.write("""
        For decades, Saudi Arabia's economy has been built overwhelmingly around its natural resource 
        endowment — vast oil reserves (Land). This has funded national infrastructure and development, 
        but has also created a economic vulnerability to oil price swings, prompting the country's 
        "Vision 2030" plan to diversify into tourism, technology, and entrepreneurship-driven sectors.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=400", caption="Saudi Arabia — Oil & Land")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1474181487882-a96a18d0771c?w=400", caption="China — Manufacturing")
    with col_text:
        st.subheader("🇨🇳 China — Labour and Capital-Driven Growth")
        st.write("""
        China's rapid growth from the 1980s onward was driven substantially by a massive, low-cost labour 
        force combined with enormous investment in capital (factories, infrastructure, ports). This combination 
        made China the "world's factory." In recent years, China has been shifting toward higher-value 
        manufacturing and technology, requiring more skilled labour and innovation (entrepreneurship).
        """)

    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.subheader("🇮🇳 India — A Growing Services and Entrepreneurship Hub")
        st.write("""
        India has leveraged a large, increasingly skilled labour force (especially in IT and services) 
        alongside a fast-growing entrepreneurial startup ecosystem — India has one of the largest numbers 
        of unicorn startups (companies valued over $1 billion) globally. The country's challenge has been 
        building enough capital (infrastructure) to fully support this labour and entrepreneurial potential.
        """)
    with col_img:
        st.image("https://images.unsplash.com/photo-1528747045269-390fe33c19f2?w=400", caption="India — Tech & Startups")

    col_img, col_text = st.columns([1, 2])
    with col_img:
        st.image("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=400", caption="USA — Innovation Hubs")
    with col_text:
        st.subheader("🇺🇸 United States — Capital and Entrepreneurship-Driven Economy")
        st.write("""
        The U.S. economy is often cited as a model of entrepreneurship-driven growth, home to major 
        innovation hubs like Silicon Valley. Deep capital markets (access to venture capital, stock markets, 
        and credit) allow entrepreneurs to raise funding relatively easily compared to many other countries, 
        fueling continuous business creation and technological innovation.
        """)

    st.subheader("🇸🇬 Singapore — Maximizing Limited Land")
    st.write("""
    Singapore has almost no natural resources and extremely limited land, yet built one of the world's 
    highest per-capita income economies by focusing intensely on **human capital** (education, skilled labour) 
    and creating a highly attractive environment for capital investment and entrepreneurship (favorable 
    business regulations, financial services hub status).
    """)

    st.info("💡 **Pattern to notice:** No country succeeds by focusing on just one factor — the most resilient economies (like the US and Singapore) tend to strategically combine skilled labour, accessible capital, and strong entrepreneurial ecosystems, rather than depending heavily on natural resource wealth (land) alone.")

# ---------------------------------------------------------
elif topic == "Modern Debates":
    st.header("🗣️ Modern Debates & Emerging Issues")
    st.write("""
    The classical four-factor model is still taught everywhere, but modern economists debate 
    how well it captures today's economy. Here are some live discussions.
    """)

    st.subheader("Is Technology/Data a Fifth Factor of Production?")
    st.write("""
    Some economists argue that **technology, information, and data** should be considered a distinct 
    fifth factor, since modern companies like Google or Meta derive enormous value from data itself, 
    separate from traditional land, labour, capital, or even a single entrepreneur's organizing skill. 
    Others argue this is simply a form of capital (intellectual capital) and doesn't need a new category.
    """)

    st.subheader("Automation and the Future of Labour")
    st.write("""
    As artificial intelligence and robotics increasingly perform tasks once requiring human labour, 
    economists debate whether this will permanently reduce the demand for human labour, or — as with 
    past technological shifts (like the Industrial Revolution) — simply shift labour toward new kinds 
    of jobs that don't exist yet. This connects directly to how the "reward" for labour (wages) 
    might change in the coming decades.
    """)

    st.subheader("Universal Basic Income (UBI) Debates")
    st.write("""
    Some propose that if capital and automation increasingly replace labour, income should be 
    partially decoupled from traditional wage-labour altogether, through policies like Universal 
    Basic Income — a direct challenge to the traditional idea that labour's reward must come strictly through wages.
    """)

    st.subheader("Environmental Limits on Land")
    st.write("""
    Climate change and resource depletion are forcing renewed attention on land as a **finite** factor. 
    Concepts like the "circular economy" (reusing materials rather than extracting new ones) and 
    carbon pricing are attempts to make economic systems account for the true scarcity and 
    environmental cost of land-based resources.
    """)

    st.subheader("The Gig Economy and Changing Labour Structures")
    st.write("""
    Platforms like ride-hailing and delivery apps have created a large class of workers who are 
    technically "independent contractors" rather than employees — raising economic and legal debates 
    about whether traditional labour protections (minimum wage, benefits) should apply to this 
    increasingly significant segment of the labour force.
    """)

    st.subheader("Entrepreneurship in the Digital Age")
    st.write("""
    Digital platforms have dramatically lowered the capital required to start a business — anyone with 
    a laptop can launch an online store or app, compared to the large capital needs of a traditional 
    factory. This has led to a surge in individual entrepreneurship (creators, freelancers, solo 
    founders) that doesn't fit neatly into older models of how entrepreneurship and capital interact.
    """)

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

    q5 = st.radio(
        "5. Who is credited with identifying Entrepreneurship as a distinct fourth factor?",
        ["Adam Smith", "David Ricardo", "Jean-Baptiste Say", "Karl Marx"],
        index=None
    )
    if q5:
        st.write("✅ Correct!" if q5 == "Jean-Baptiste Say" else "❌ Not quite — **Jean-Baptiste Say** is credited with this.")

    q6 = st.radio(
        "6. What did Joseph Schumpeter call the process where new innovations make old industries obsolete?",
        ["Creative destruction", "Diminishing returns", "Comparative advantage", "Surplus value"],
        index=None
    )
    if q6:
        st.write("✅ Correct!" if q6 == "Creative destruction" else "❌ Not quite — Schumpeter called this **'Creative destruction.'**")

    q7 = st.radio(
        "7. According to Frank Knight, entrepreneurial profit is the reward for bearing what?",
        ["Insurable risk", "Uninsurable uncertainty", "Wage costs", "Land scarcity"],
        index=None
    )
    if q7:
        st.write("✅ Correct!" if q7 == "Uninsurable uncertainty" else "❌ Not quite — Knight argued profit rewards **uninsurable uncertainty**, distinct from measurable risk.")

st.divider()
st.caption("Built to explain the Factors of Production: Land, Labour, Capital, and Entrepreneurship — with historical, theoretical, and global context.")

