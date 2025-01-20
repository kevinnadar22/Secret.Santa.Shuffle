function showRaffleAnimation(matchName, wishlist = '') {
    const overlay = document.createElement('div');
    overlay.className = 'raffle-overlay';
    overlay.innerHTML = `
        <div class="gift-box">
            <div class="gift-bow">
                <div class="bow-left"></div>
                <div class="bow-right"></div>
            </div>
            <div class="gift-lid"></div>
            <div class="gift-box-main">
                <div class="gift-ribbon"></div>
                <div class="countdown"></div>
            </div>
            <div class="match-card">
                <div class="match-card-content">
                    <h2 class="text-3xl font-bold mb-4">🎄 Your Secret Santa Match 🎄</h2>
                    <p class="text-4xl font-bold text-red-600 mb-4">${matchName}</p>
                    ${wishlist ? `
                    <div class="wishlist-section">
                        <h4 class="text-lg font-bold mb-2">They're hoping for...</h4>
                        <p class="text-lg text-amber-800">${wishlist}</p>
                    </div>
                    ` : ''}
                </div>
                <div class="click-hint">Click anywhere to close</div>
            </div>
        </div>
    `;
    document.body.appendChild(overlay);

    // Create confetti
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.background = ['#ff4444', '#ffdd44', '#44ff44', '#4444ff'][Math.floor(Math.random() * 4)];
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.top = -20 + 'px';
        overlay.appendChild(confetti);
    }

    const tl = gsap.timeline();

    // Initial fade in
    tl.to(overlay, { opacity: 1, duration: 0.5 })
        .to('.gift-box', { scale: 1.2, duration: 1, ease: 'elastic.out(1, 0.5)' });

    // Countdown animation
    let count = 3;
    const countEl = overlay.querySelector('.countdown');

    function showNumber() {
        if (count > 0) {
            // Prepare the number
            countEl.textContent = count;

            // Complex animation sequence
            gsap.timeline()
                .to(countEl, {
                    opacity: 1,
                    duration: 0.3,
                    ease: 'power2.out'
                })
                .from(countEl, {
                    scale: 2,
                    duration: 0.6,
                    ease: 'elastic.out(1, 0.5)',
                }, '-=0.3')
                // Fancy gift box animation
                .to('.gift-box', {
                    keyframes: [
                        { rotation: -3, duration: 0.1 },
                        { rotation: 3, duration: 0.1 },
                        { rotation: -2, duration: 0.1 },
                        { rotation: 2, duration: 0.1 },
                        { rotation: 0, duration: 0.1 }
                    ],
                    ease: 'none'
                }, '-=0.4')
                // Fade out
                .to(countEl, {
                    opacity: 0,
                    scale: 0.5,
                    duration: 0.3,
                    ease: 'power2.in',
                    delay: 0.2
                });

            count--;
            setTimeout(showNumber, 1000);
        } else {
            // Enhanced gift opening animation
            const openingTl = gsap.timeline();

            openingTl
                .to('.gift-lid', {
                    rotationX: -180,
                    duration: 1.2,
                    ease: 'power4.inOut'
                })
                .to('.gift-bow', {
                    y: -30,
                    opacity: 0,
                    duration: 0.6,
                    ease: 'power2.in'
                }, '-=1')
                .to('.countdown', {
                    opacity: 0,
                    scale: 0,
                    duration: 0.3,
                    ease: 'power2.in'
                }, '-=0.8')
                // Enhanced match card reveal
                .to('.match-card', {
                    opacity: 1,
                    scale: 1,
                    y: 0,
                    duration: 1.2,
                    ease: 'elastic.out(1, 0.5)',
                    onComplete: () => {
                        // Show click hint with animation
                        gsap.to('.click-hint', {
                            opacity: 1,
                            y: 0,
                            duration: 0.5,
                            delay: 0.5
                        });
                    }
                });

            // Enhanced confetti animation
            gsap.to('.confetti', {
                opacity: 1,
                y: '100vh',
                rotation: 'random(-720, 720)',
                x: 'random(-200, 200)',
                duration: 'random(2, 4)',
                stagger: {
                    amount: 2,
                    from: 'random'
                },
                ease: 'power1.out'
            });

            // Smooth floating animation
            gsap.to('.gift-box', {
                y: '-=30',
                duration: 2,
                yoyo: true,
                repeat: -1,
                ease: 'power1.inOut'
            });
        }
    }

    // Start countdown
    setTimeout(showNumber, 500);

    // Add click handler to close overlay
    overlay.addEventListener('click', () => {
        gsap.to('.match-card', {
            scale: 0.8,
            opacity: 0,
            duration: 0.3,
            ease: 'power2.in'
        });
        gsap.to(overlay, {
            opacity: 0,
            duration: 0.3,
            onComplete: () => overlay.remove()
        });
    });
}
