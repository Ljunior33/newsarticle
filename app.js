// Travel Tailor Interactive Presentation JS - Improved Navigation

class PresentationController {
  constructor() {
    this.TOTAL_SLIDES = 8;
    this.currentSlide = 0;

    // Cache DOM elements
    this.slides = Array.from(document.querySelectorAll('.slide'));
    this.indicators = Array.from(document.querySelectorAll('.indicator'));
    this.progressFill = document.getElementById('progressFill');
    this.prevBtn = document.getElementById('prevBtn');
    this.nextBtn = document.getElementById('nextBtn');

    // Guard clause if crucial elements missing
    if (!this.slides.length || !this.indicators.length) return;

    this.bindEvents();
    this.showSlide(0);
  }

  bindEvents() {
    this.prevBtn.addEventListener('click', () => this.previousSlide());
    this.nextBtn.addEventListener('click', () => this.nextSlide());

    // Indicator click
    this.indicators.forEach((indicator, idx) => {
      indicator.addEventListener('click', () => this.goToSlide(idx));
    });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ') {
        e.preventDefault();
        this.nextSlide();
      } else if (e.key === 'ArrowLeft') {
        e.preventDefault();
        this.previousSlide();
      }
    });
  }

  showSlide(idx) {
    if (idx < 0 || idx >= this.TOTAL_SLIDES) return;

    // Update slide visibility
    this.slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === idx);
    });

    // Update indicators
    this.indicators.forEach((ind, i) => {
      ind.classList.toggle('active', i === idx);
    });

    // Update buttons
    this.prevBtn.disabled = idx === 0;
    this.nextBtn.disabled = idx === this.TOTAL_SLIDES - 1;

    // Progress bar
    const percent = ((idx + 1) / this.TOTAL_SLIDES) * 100;
    this.progressFill.style.width = `${percent}%`;

    this.currentSlide = idx;
  }

  nextSlide() {
    if (this.currentSlide < this.TOTAL_SLIDES - 1) {
      this.showSlide(this.currentSlide + 1);
    }
  }

  previousSlide() {
    if (this.currentSlide > 0) {
      this.showSlide(this.currentSlide - 1);
    }
  }

  goToSlide(idx) {
    this.showSlide(idx);
  }
}

// Init when DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new PresentationController());
} else {
  new PresentationController();
}