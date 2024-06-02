---
marp: true
theme: gaia
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.svg')
style: |
  .author-list {
    line-height: 0.7;
  }
  .container {
    display: flex;
    justify-content: space-between;
  }
  .column {
    flex: 1;
    padding: 0 10px;
  }
  .left-text {
    text-align: left;
  }
---

<img src="img/conference_logo.jpg" width="15%" />

### Generating Music Variations through Chaotic Dynamical Systems Exploration

###### Rajamangala University of Technology Thanyaburi

<div class="author-list">
  <h6>Kanatsanun Sub-udom</h6>
  <h6>Wannasa Rianthong</h6>
  <h6>Patipan Somwong</h6>
</div>

---

### Nowaday Music AI 
artificial intelligence (AI) technologies have significantly advanced, enabling them to create music with ever-increasing proficiency. 
Well-known AI music generation platforms such as Mubert, Soundraw and AIVA


| <h5>Pros</h5>    | <h5>Cons</h5> |
| -------- | ------- |
| <h6>User friendly</h6>  | <h6>Require high computational resources</h6>    |
| <h6>Easily accessible online</h6> | <h6>May produce music in limited styles</h6>    |

---

#### Introduce to Dabby Musical Variations from a Chaotic Mapping Method

The Lorenz system, a dynamical system with parameters $\sigma > 0$, $r > 0$ and $b > 0$ given by:

$$
\begin{aligned}
\dot{x}_1 &= \sigma(x_2 - x_1) \\
\dot{x}_2 &= rx_1 - x_2 - x_1x_3 \\
\dot{x}_3 &= x_1x_2 - bx_3
\end{aligned}
$$

if parameters set to $\sigma = 10$, $r = 28$ and $b = \dfrac{8}{3}$, it exhibits chaotic behavior.

---

![bg right 100%](img/dabby_process.png)

#### Process of Dabby Musical Variations Method

<center>
<h6>Original Variation</h6>
  <img src="img/dabby_1.png" width="100%" />
  <audio controls>
    <source src="mp3/dabby_1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

<center>
<h6>New Variation</h6>
  <img src="img/dabby_2.png" width="100%" />
  <audio controls>
    <source src="mp3/dabby_2.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

---

### Introduce to Melodic Variation with Expanded Rhythm Method
This technique extends the rhythmic duration of musical notes, thereby opening up a number of possibilities for creating new musical variations.

<div class="container">
  <div class="column">
    <center>
    <h6>Original Variation</h6>
      <img src="img/er_1.png" width="45%" />
      <audio controls>
        <source src="mp3/er_1.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
    <h6>Expanded Rhythm</h6>
      <img src="img/er_12.png" width="100%" />
      <audio controls>
        <source src="mp3/er_12.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>

---

![bg right 100%](img/er_process.png)

#### Process of Expanded Rhythm Method

<center>
<h6>Original Variation</h6>
  <img src="img/er_1.png" width="45%" />
  <audio controls>
    <source src="mp3/er_1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

<center>
<h6>New Variation</h6>
  <img src="img/er_2.png" width="100%" />
  <audio controls>
    <source src="mp3/er_2.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
  </audio>
</center>

---

### Example from Expanded Rhythm Method

<br>

<center>
Pachelbel Canon in D
</center>

<div class="container">
  <div class="column">
    <center>
    <h6>Original Variation</h6>
      <audio controls>
        <source src="mp3/original_cnd.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
    <h6>New Variation</h6>
      <audio controls>
        <source src="mp3/new_cnd.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>

<br>

<center>
Yiruma, (이루마) - River Flows in You
</center>
<div class="container">
  <div class="column">
    <center>
    <h6>Original Variation</h6>
      <audio controls>
        <source src="mp3/original_rfiy.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
  <div class="column">
    <center>
    <h6>New Variation</h6>
      <audio controls>
        <source src="mp3/new_rfiy.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
      </audio>
    </center>
  </div>
</div>

---

### Future Approach

<h6> Melodic variation </h6>
<img src="img/melodic_variation.png" width="100%" />
<h6> Rhythmic variation </h6>
<img src="img/rhythmic_variation.png" width="100%" />
