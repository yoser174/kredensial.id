/**
 * Tagify Users
 */

'use strict';

(async function () {
  // Users List suggestion
  //------------------------------------------------------
  const TagifyUserListEl = document.querySelector('#TagifyUserList');


  try {
    const request = await fetch("/api/users/?format=json");
    if (!request.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await request.json();
    const usersList = json.results;


  function tagTemplate(tagData) {
    return `
    <tag title="${tagData.title || tagData.email}"
      contenteditable='false'
      spellcheck='false'
      tabIndex="-1"
      class="${this.settings.classNames.tag} ${tagData.class ? tagData.class : ''}"
      ${this.getAttributes(tagData)}
    >
      <x title='' class='tagify__tag__removeBtn' role='button' aria-label='remove tag'></x>
      <div>
        <div class='tagify__tag__avatar-wrap'>
          <img onerror="this.style.visibility='hidden'" src="${tagData.avatar}">
        </div>
        <span class='tagify__tag-text'>${tagData.name}</span>
      </div>
    </tag>
  `;
  }

  function suggestionItemTemplate(tagData) {
    return `
    <div ${this.getAttributes(tagData)}
      class='tagify__dropdown__item align-items-center ${tagData.class ? tagData.class : ''}'
      tabindex="0"
      role="option"
    >
      ${
        tagData.avatar
          ? `<div class='tagify__dropdown__item__avatar-wrap'>
          <img onerror="this.style.visibility='hidden'" src="${tagData.avatar}">
        </div>`
          : ''
      }
      <div class="fw-medium">${tagData.name}</div>
      <span>${tagData.email}</span>
    </div>
  `;
  }
  function dropdownHeaderTemplate(suggestions) {
    // return `
    //     <div class="${this.settings.classNames.dropdownItem} ${this.settings.classNames.dropdownItem}__addAll">
    //         <strong>${this.value.length ? `Add remaning` : 'Add All'}</strong>
    //         <span>${suggestions.length} members</span>
    //     </div>
    // `;
    return '';
  }

  // initialize Tagify on the above input node reference
  let TagifyUserList = new Tagify(TagifyUserListEl, {
    tagTextProp: 'name', // very important since a custom template is used with this property as text. allows typing a "value" or a "name" to match input with whitelist
    enforceWhitelist: true,
    skipInvalid: true, // do not remporarily add invalid tags
    dropdown: {
      closeOnSelect: false,
      enabled: 0,
      classname: 'users-list',
      searchKeys: ['name', 'email'] // very important to set by which keys to search for suggesttions when typing
    },
    templates: {
      tag: tagTemplate,
      dropdownItem: suggestionItemTemplate,
      dropdownHeader: dropdownHeaderTemplate
    },
    whitelist: usersList
  });

  // attach events listeners
  TagifyUserList.on('dropdown:select', onSelectSuggestion) // allows selecting all the suggested (whitelist) items
    .on('edit:start', onEditStart); // show custom text in the tag while in edit-mode

  function onSelectSuggestion(e) {
    // custom class from "dropdownHeaderTemplate"
    if (e.detail.elm.classList.contains(`${TagifyUserList.settings.classNames.dropdownItem}__addAll`))
      TagifyUserList.dropdown.selectAll();
  }

  function onEditStart({ detail: { tag, data } }) {
    TagifyUserList.setTagTextNode(tag, `${data.name} <${data.email}>`);
  }

  // Email List suggestion
  //------------------------------------------------------
  // generate random whitelist items (for the demo)
  let randomStringsArr = Array.apply(null, Array(100)).map(function () {
    return (
      Array.apply(null, Array(~~(Math.random() * 10 + 3)))
        .map(function () {
          return String.fromCharCode(Math.random() * (123 - 97) + 97);
        })
        .join('') + '@gmail.com'
    );
  });

  const TagifyEmailListEl = document.querySelector('#TagifyEmailList'),
    TagifyEmailList = new Tagify(TagifyEmailListEl, {
      // email address validation (https://stackoverflow.com/a/46181/104380)
      pattern:
        /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
      whitelist: randomStringsArr,
      callbacks: {
        invalid: onInvalidTag
      },
      dropdown: {
        position: 'text',
        enabled: 1 // show suggestions dropdown after 1 typed character
      }
    }),
    button = TagifyEmailListEl.nextElementSibling; // "add new tag" action-button

  button.addEventListener('click', onAddButtonClick);

  function onAddButtonClick() {
    TagifyEmailList.addEmptyTag();
  }

  function onInvalidTag(e) {
    console.log('invalid', e.detail);
  }


  } catch (error) {
    console.error(error.message);
  }
})();
