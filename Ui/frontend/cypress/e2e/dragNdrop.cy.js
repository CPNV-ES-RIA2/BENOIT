describe('Drag and drop image', () => {
    it('Image appears in preview after dropping', () => {
        cy.visit('http://localhost:5173');

        const filePath = 'Egger.jpeg';

        cy.get('.dropzone').as('dropZone');

        cy.fixture(filePath, 'base64').then((fileContent) => {
            cy.get('@dropZone').trigger('drop', {
                dataTransfer: {
                    files: [{
                        name: 'image.jpg',
                        type: 'image/jpeg',
                        blob: Cypress.Blob.base64StringToBlob(fileContent, 'image/jpeg')
                    }]
                }
            });
        });

        cy.get('#preview-image').should('be.visible');
    });
});
