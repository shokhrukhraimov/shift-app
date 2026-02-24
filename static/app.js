const tg = window.Telegram.WebApp;
tg.expand(); // WebAppni to'liq ochish

const container = document.getElementById("days-container");
const now = new Date();
const currentMonth = now.getMonth();
const currentYear = now.getFullYear();
const todayDate = now.getDate();

// Oyning kunlari sonini aniqlash
const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();

for (let i = 1; i <= daysInMonth; i++) {
    const dayDiv = document.createElement("div");
    dayDiv.classList.add("day-card");

    // Holatni aniqlash (o'tgan, bugun, kelajak)
    if (i < todayDate) dayDiv.classList.add("past");
    else if (i === todayDate) dayDiv.classList.add("today");
    else dayDiv.classList.add("future");

    dayDiv.innerHTML = `
        <div class="day-title">
            <span>${i}-fevral</span>
            <span>${i === todayDate ? "📌 Bugun" : ""}</span>
        </div>
        <div class="shift-content">
            <strong>Smenalar:</strong><br>
            ☀️ Kunduzgi: Ali, Vali<br>
            🌙 Tunggi: G'ani, Sani
        </div>
    `;

    // Accordion bosilganda ochilishi
    dayDiv.onclick = () => {
        const content = dayDiv.querySelector(".shift-content");
        const isOpen = content.style.display === "block";
        
        // Hammasini yopib, faqat tanlanganini ochish
        document.querySelectorAll('.shift-content').forEach(c => c.style.display = 'none');
        content.style.display = isOpen ? "none" : "block";
    };

    container.appendChild(dayDiv);
}