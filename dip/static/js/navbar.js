var current_url = window.location.pathname;

var menu_items = document.querySelectorAll('.navbar__menu-item');

for (const item of menu_items) {
  const menu_item_url = item.children[0].getAttribute('href');

  if (current_url === menu_item_url) {
    item.classList.add('navbar__menu-item-active');
  }
}