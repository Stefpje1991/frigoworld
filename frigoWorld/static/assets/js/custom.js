document.addEventListener('DOMContentLoaded', function() {
  // Haal de filters op
  const categoryRadios = document.querySelectorAll('input[name="category"]');
  console.log(categoryRadios)
  const container = document.querySelector('.row'); // De container waar de kaarten komen te staan

  // Voeg event listeners toe voor de radiobuttons
  categoryRadios.forEach(radio => {
    radio.addEventListener('change', function() {
      filterItems();
    });
  });

  // Functie om de items te filteren en opnieuw weer te geven
  function filterItems() {
    const selectedCategory = document.querySelector('input[name="category"]:checked')?.value || 'all';
    console.log(selectedCategory)

    // Haal alle kaarten op
    const allCards = document.querySelectorAll('.card');
    console.log(allCards)
    // Filter de kaarten op basis van de geselecteerde filters
    allCards.forEach(card => {
      const itemCategory = card.getAttribute('data-category');
      console.log(itemCategory)

      // Controleer of de kaart voldoet aan de geselecteerde filters
      const categoryMatch = (itemCategory === selectedCategory || selectedCategory === 'all');

      // Als de kaart voldoet aan de filters, toon de kaart, anders verberg deze
      if (categoryMatch) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // Initialiseer de filtering bij het laden van de pagina
  filterItems();
});
