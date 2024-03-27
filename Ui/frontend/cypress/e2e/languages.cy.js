describe('Change languages', () => {
    it('Language changes to French', () => {
        cy.visit('http://localhost:5173');

        cy.get('h1#title').should('have.text', 'Image to Labels');

        cy.get('button#lang-fr').click();

        cy.get('h1#title').should('have.text', 'Image en étiquettes');
    });
});
