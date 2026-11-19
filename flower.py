"""
Love Letter  -  full version (Python + tkinter, nothing to install)
Run:  python love_letter_full.py

1. Click "Open Letter": envelope opens, letter rises, a flower blooms and
   "CAN YOU BE MY GIRLFRIEND?" appears in rainbow colors.
2. She types her name in the box at the bottom.
3. The "Yes" and "No" buttons appear on the letter.
   - No  -> the button runs away around the letter and can't be clicked.
   - Yes -> a cute cat holding a flower appears with hearts everywhere.
"""
import tkinter as tk
import math, random, colorsys

W, H = 700, 640
YES_POS = (270, 485)
NO_START = (430, 485)
NO_LABELS = ["No", "Nope!", "Too slow!", "Catch me!", "Missed!", "Hehe"]


def color(h, s=0.75, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1, s, v)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))


def clamp(x):
    return max(0.0, min(1.0, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def lerp(a, b, t):
    return a + (b - a) * t


def heart(cx, cy, s):
    pts = []
    for i in range(0, 360, 12):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts += [cx + x * s, cy - y * s]
    return pts


def petal(cx, cy, ang, d, length, width):
    pts = []
    for k in range(0, 360, 30):
        t = math.radians(k)
        u = d + length / 2 + (length / 2) * math.cos(t)
        v = (width / 2) * math.sin(t)
        pts += [cx + u * math.cos(ang) - v * math.sin(ang),
                cy + u * math.sin(ang) + v * math.cos(ang)]
    return pts


def rotator(px, py, deg):
    a = math.radians(deg)
    ca, sa = math.cos(a), math.sin(a)
    return lambda x, y: (px + (x - px) * ca - (y - py) * sa,
                         py + (x - px) * sa + (y - py) * ca)


class LoveLetter:
    def __init__(self, root):
        self.root = root
        root.title("A Letter For You")
        root.resizable(False, False)
        root.configure(bg="#2b1030")
        self.c = tk.Canvas(root, width=W, height=H, highlightthickness=0, bg="#2b1030")
        self.c.pack()

        # ---- bottom bar: name box + buttons ----
        bar = tk.Frame(root, bg="#2b1030")
        bar.pack(fill="x", pady=8)
        tk.Label(bar, text="Her name:", bg="#2b1030", fg="#ffd9e8",
                 font=("Georgia", 13, "italic")).pack(side="left", padx=(14, 4))
        self.name_var = tk.StringVar()
        tk.Entry(bar, textvariable=self.name_var, font=("Arial", 14), width=13,
                 justify="center").pack(side="left")
        tk.Button(bar, text="Send Love", font=("Arial", 13, "bold"), bg="#ffb703",
                  fg="#3a1030", relief="flat", padx=12, pady=4,
                  command=self.burst).pack(side="right", padx=14)
        self.btn = tk.Button(bar, text="Open Letter", font=("Arial", 13, "bold"),
                             bg="#ff4f81", fg="white", activebackground="#ff7aa2",
                             relief="flat", padx=14, pady=4, command=self.toggle)
        self.btn.pack(side="right")

        # ---- Yes / No / Back buttons (live on the canvas) ----
        self.yes_btn = tk.Button(self.c, text="Yes ♥", font=("Arial", 14, "bold"),
                                 bg="#ff4f81", fg="white", relief="flat", padx=16,
                                 pady=3, command=self.say_yes)
        self.no_btn = tk.Button(self.c, text="No", font=("Arial", 14, "bold"),
                                bg="#8a8a99", fg="white", relief="flat", padx=16, pady=3)
        self.back_btn = tk.Button(self.c, text="Back to the letter", font=("Arial", 13, "bold"),
                                  bg="#ff4f81", fg="white", relief="flat", padx=14,
                                  pady=4, command=self.back)
        # the No button can never be clicked: it runs away
        self.no_btn.bind("<Enter>", self.dodge)
        self.no_btn.bind("<Motion>", self.dodge)
        self.no_btn.bind("<Button-1>", lambda e: (self.dodge(), "break")[1])
        self.yes_win = self.c.create_window(*YES_POS, window=self.yes_btn, state="hidden")
        self.no_win = self.c.create_window(*NO_START, window=self.no_btn, state="hidden")
        self.back_win = self.c.create_window(W // 2, 598, window=self.back_btn, state="hidden")

        self.c.bind("<Button-1>", lambda e: self.burst(e.x, e.y, 18))
        self.c.bind("<Motion>", self.on_move)

        self.p = 0.0
        self.target = 0
        self.t = 0.0
        self.frame = 0
        self.yes = False
        self.no_x, self.no_y = NO_START
        self.no_tx, self.no_ty = NO_START
        self.no_n = 0
        self.hearts = []
        self.stars = [(random.randint(0, W), random.randint(0, H), random.random() * 6)
                      for _ in range(60)]
        self.tick()

    # ---------- canvas helpers (everything drawn gets the tag "scene") ----------
    def oval(self, *a, **k): return self.c.create_oval(*a, tags="scene", **k)
    def poly(self, *a, **k): return self.c.create_polygon(*a, tags="scene", **k)
    def rect(self, *a, **k): return self.c.create_rectangle(*a, tags="scene", **k)
    def line(self, *a, **k): return self.c.create_line(*a, tags="scene", **k)
    def text(self, *a, **k): return self.c.create_text(*a, tags="scene", **k)

    # ---------- actions ----------
    @property
    def name(self):
        return self.name_var.get().strip()

    @property
    def ready(self):
        return self.target == 1 and self.p >= 0.999 and self.name != "" and not self.yes

    def toggle(self):
        self.target = 1 - self.target
        self.yes = False
        self.btn.config(text="Close Letter" if self.target else "Open Letter")

    def burst(self, x=W // 2, y=H // 2, n=30):
        for _ in range(n):
            self.hearts.append(dict(x=x, y=y, s=random.uniform(0.4, 1.0),
                                    vx=random.uniform(-3.5, 3.5), vy=random.uniform(-7, -1),
                                    hue=random.random(), ph=random.random() * 6, burst=True))

    def say_yes(self):
        self.yes = True
        self.burst(W // 2, H // 2, 60)

    def back(self):
        self.yes = False

    def dodge(self, e=None):
        x, y = self.no_tx, self.no_ty
        for _ in range(40):
            x, y = random.randint(235, 465), random.randint(90, 495)
            if (math.hypot(x - YES_POS[0], y - YES_POS[1]) > 90
                    and math.hypot(x - self.no_tx, y - self.no_ty) > 120):
                break
        self.no_tx, self.no_ty = x, y
        self.no_n += 1
        self.no_btn.config(text=NO_LABELS[self.no_n % len(NO_LABELS)])

    def on_move(self, e):
        if self.ready and math.hypot(e.x - self.no_x, e.y - self.no_y) < 80:
            self.dodge()

    # ---------- animation loop ----------
    def tick(self):
        self.t += 0.04
        self.frame += 1
        step = 0.012
        if self.p < self.target:
            self.p = min(1, self.p + step)
        elif self.p > self.target:
            self.p = max(0, self.p - step * 1.5)

        # show / hide the canvas buttons
        show = "normal" if self.ready else "hidden"
        self.c.itemconfigure(self.yes_win, state=show)
        self.c.itemconfigure(self.no_win, state=show)
        self.c.itemconfigure(self.back_win, state="normal" if self.yes else "hidden")
        if not self.ready:
            self.no_x, self.no_y = NO_START
            self.no_tx, self.no_ty = NO_START
        else:  # glide toward the target spot
            self.no_x += (self.no_tx - self.no_x) * 0.35
            self.no_y += (self.no_ty - self.no_y) * 0.35
        self.c.coords(self.no_win, self.no_x, self.no_y)

        # hearts
        if (self.p > 0.7 or self.yes) and random.random() < 0.25:
            self.hearts.append(dict(x=random.randint(20, W - 20), y=H + 20,
                                    s=random.uniform(0.4, 1.0), vx=0,
                                    vy=random.uniform(1, 2.5), hue=random.random(),
                                    ph=random.random() * 6, burst=False))
        if self.yes and self.frame % 20 == 0:
            self.burst(random.randint(60, W - 60), random.randint(300, 520), 10)
        for h in self.hearts:
            if h["burst"]:
                h["vy"] += 0.1
                h["x"] += h["vx"]
                h["y"] += h["vy"]
            else:
                h["x"] += math.sin(self.t + h["ph"]) * 0.8
                h["y"] -= h["vy"]
        self.hearts = [h for h in self.hearts if -30 < h["y"] < H + 40]

        self.draw()
        self.root.after(30, self.tick)

    # ---------- drawing ----------
    def draw(self):
        c, t = self.c, self.t
        c.delete("scene")
        self.rect(0, 0, W, H, fill=color(0.85 + 0.03 * math.sin(t * 0.5), 0.6, 0.22), outline="")
        for x, y, ph in self.stars:
            r = 1.5 + 1.5 * abs(math.sin(t * 1.5 + ph))
            self.oval(x - r, y - r, x + r, y + r, fill="#ffe9f3", outline="")

        if self.yes:
            self.draw_yes()
        else:
            self.draw_envelope()

        for h in self.hearts:
            s = h["s"] * (1 + 0.1 * math.sin(t * 4 + h["ph"]))
            self.poly(heart(h["x"], h["y"], s * 1.4), smooth=True,
                      fill=color(h["hue"] + t * 0.05, 0.6, 1), outline="")

    def draw_envelope(self):
        p, t = self.p, self.t
        flap = ease(p / 0.3)
        rise = ease((p - 0.25) / 0.45)
        down = ease((p - 0.6) / 0.4)
        grow = ease((p - 0.7) / 0.3)

        dy = 230 * down
        top, bottom = 330 + dy, 560 + dy
        tip = lerp(450, 215, flap) + dy

        self.rect(150, top, 550, bottom, fill="#c2325f", outline="#8e1f45", width=2)
        if flap > 0.5:
            self.poly(150, top, 550, top, 350, tip, fill="#a82a52", outline="#8e1f45", width=2)

        y_top = lerp(520, 40, rise)
        if p > 0.2:
            y_bot = min(y_top + 480, bottom - 10)
            self.rect(190, y_top, 510, y_bot, fill="#fff8e7", outline="#e8c9a0", width=2)
            if grow > 0:
                self.draw_letter_content(y_top, grow)

        self.poly(150, top, 350, top + 130, 550, top, 550, bottom, 150, bottom,
                  fill="#f06292", outline="#8e1f45", width=2)
        if flap <= 0.5:
            self.poly(150, top, 550, top, 350, tip, fill="#e0457b", outline="#8e1f45", width=2)
            if p < 0.05:
                self.poly(heart(350, tip - 8, 2.2), fill="#ffd166", outline="#b8860b")

        if p < 0.05:
            self.text(W // 2, 150, text="You have a letter...", fill="#ffd1e3",
                      font=("Georgia", 26, "italic"))
            self.text(W // 2, 200, text="press the button", fill="#ff9ec4",
                      font=("Georgia", 16))

    def draw_letter_content(self, y_top, g):
        t = self.t
        self.text(350, y_top + 26, text="~ For You ~", fill="#c2325f", font=("Georgia", 15, "italic"))
        cx, cy = 350, y_top + 145
        s = g * 0.9
        sway = math.sin(t) * 6 * s
        stem_bot = y_top + 275
        self.line(cx, cy, cx + sway, cy + (stem_bot - cy) * g, fill="#2e9e4f", width=6, smooth=True)
        for side in (-1, 1):
            lx = cx + side * 32 * s + sway / 2
            ly = cy + 100 * s
            self.poly(cx + sway / 3, ly + 18, lx, ly - 9, lx + side * 14, ly + 9,
                      fill="#3fc46b", outline="#2e9e4f", smooth=True)
        for ring, (n, d, L, W_, v) in enumerate([(10, 14, 82, 38, 0.9), (8, 8, 52, 28, 1.0)]):
            for i in range(n):
                ang = i * 2 * math.pi / n + t * (0.25 if ring == 0 else -0.35)
                col = color(i / n + t * 0.08 + ring * 0.15, 0.65 if ring == 0 else 0.5, v)
                self.poly(petal(cx, cy, ang, d * s, L * s, W_ * s), smooth=True,
                          fill=col, outline="#ffffff")
        r = 20 * s * (1 + 0.06 * math.sin(t * 5))
        self.oval(cx - r, cy - r, cx + r, cy + r, fill="#ffcc00", outline="#ff9900", width=2)

        # rainbow question, three lines
        size = int(26 * (1 + 0.08 * math.sin(t * 4)) * g)
        if size > 2:
            idx = 0
            for row, word in enumerate(["CAN YOU", "BE MY", "GIRLFRIEND?"]):
                y0 = y_top + 305 + row * 33
                x0 = 350 - len(word) * 21 / 2 + 10
                for i, ch in enumerate(word):
                    idx += 1
                    if ch == " ":
                        continue
                    x = x0 + i * 21
                    y = y0 + math.sin(t * 3 + idx) * 4
                    self.text(x + 2, y + 2, text=ch, fill="#aa8899", font=("Arial", size, "bold"))
                    self.text(x, y, text=ch, fill=color(idx / 20 + t * 0.2, 0.85, 1),
                              font=("Arial", size, "bold"))
        if self.name:
            self.text(350, y_top + 398, text="For %s ♥" % self.name, fill="#c2325f",
                      font=("Georgia", 14, "italic"))
        if self.p >= 0.999 and not self.name:
            self.text(350, y_top + 445, text="Write your name below to answer ♥",
                      fill="#c2325f", font=("Georgia", 13, "italic"))

    def draw_yes(self):
        t = self.t
        k = 1.4
        ox, oy = 350 - 135 * k, 125
        by = math.sin(t * 3) * 6
        OR, DK = "#ffb86b", "#e8893a"

        def X(x): return ox + x * k
        def Y(y): return oy + y * k + by

        def P(pts, rot=None):
            out = []
            for x, y in pts:
                if rot:
                    x, y = rot(x, y)
                out += [X(x), Y(y)]
            return out

        def oval(cx, cy, rx, ry, **kw):
            self.oval(X(cx - rx), Y(cy - ry), X(cx + rx), Y(cy + ry), **kw)

        self.text(W // 2, 52, text="Yay! Thank you, %s! ♥" % self.name, fill="#ffd9e8",
                  font=("Georgia", 26, "italic"))
        self.text(W // 2, 92, text="You just made me the happiest person ever.",
                  fill="#ff9ec4", font=("Georgia", 14))

        # tail (wagging), body, belly, feet
        wag = rotator(70, 245, math.sin(t * 5) * 14)
        self.line(P([(70, 245), (30, 255), (8, 215), (35, 168)], wag), smooth=True,
                  width=16 * k, fill=OR, capstyle="round")
        oval(120, 205, 58, 58, fill=OR, outline="")
        oval(120, 215, 34, 38, fill="#ffe3bf", outline="")
        oval(90, 262, 22, 11, fill=OR, outline=DK, width=2)
        oval(150, 262, 22, 11, fill=OR, outline=DK, width=2)

        # flower held in the paw (sways)
        sw = rotator(212, 255, math.sin(t * 2.5) * 5)
        self.line(P([(212, 160), (212, 255)], sw), width=5 * k, fill="#2e9e4f", capstyle="round")
        self.poly(P([(212, 235), (232, 222), (248, 230), (250, 244), (232, 248), (218, 244)], sw),
                  smooth=True, fill="#3fc46b", outline="")
        for i in range(7):
            pp = petal(212, 150, i * 2 * math.pi / 7 + t * 0.5, 9, 30, 20)
            self.poly(P(list(zip(pp[0::2], pp[1::2])), sw), smooth=True,
                      fill=color(i / 7 + t * 0.1, 0.6, 1), outline="#ffffff")
        fx, fy = sw(212, 150)
        oval(fx, fy, 9, 9, fill="#ffcc00", outline="#ff9900", width=2)

        # head + ears + stripes
        oval(120, 120, 70, 58, fill=OR, outline="")
        self.poly(P([(62, 88), (68, 30), (110, 66)]), fill=OR, outline="")
        self.poly(P([(178, 88), (172, 30), (130, 66)]), fill=OR, outline="")
        self.poly(P([(72, 76), (75, 48), (96, 66)]), fill="#ff9ab8", outline="")
        self.poly(P([(168, 76), (165, 48), (144, 66)]), fill="#ff9ab8", outline="")
        for a, b in [((120, 64), (120, 78)), ((103, 68), (106, 80)), ((137, 68), (134, 80))]:
            self.line(P([a, b]), fill=DK, width=4 * k, capstyle="round")

        # eyes (they blink), cheeks, nose, mouth, whiskers
        bl = 0.1 if int(t * 10) % 60 < 2 else 1
        for ex in (92, 148):
            oval(ex, 122, 11, 14 * bl, fill="#2b1030", outline="")
            if bl > 0.5:
                oval(ex + 4, 116, 4.5, 4.5, fill="#ffffff", outline="")
                oval(ex - 3, 128, 2, 2, fill="#ffffff", outline="")
        oval(68, 142, 12, 7, fill="#ff9fb8", outline="")
        oval(172, 142, 12, 7, fill="#ff9fb8", outline="")
        self.poly(P([(114, 138), (126, 138), (120, 146)]), fill="#ff7a9c", outline="")
        for sx in (-1, 1):
            self.line(P([(120, 146), (120 + sx * 5, 152), (120 + sx * 15, 148)]), smooth=True,
                      fill="#7a3a2a", width=2.5, capstyle="round")
            for dy in (0, 8):
                self.line(P([(120 + sx * 58, 134 + dy), (120 + sx * 84, 128 + dy * 1.8)]),
                          fill="#7a3a2a", width=1.8)

        # arms + paw gripping the flower
        self.line(P([(72, 192), (60, 220), (80, 240)]), smooth=True, width=22 * k,
                  fill=OR, capstyle="round")
        self.line(P([(168, 192), (195, 196), (207, 214)]), smooth=True, width=22 * k,
                  fill=OR, capstyle="round")
        oval(212, 216, 13, 13, fill=OR, outline=DK, width=2)


if __name__ == "__main__":
    root = tk.Tk()
    LoveLetter(root)
    root.mainloop()