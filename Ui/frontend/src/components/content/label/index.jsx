import React from 'react';
import { useTranslation } from 'react-i18next';

export default function Label({ response }) {
    const { t } = useTranslation();

    // Ensure response is in the expected format and is not undefined
    const isValidResponse = Array.isArray(response);

    return (
        <div className="w-full flex justify-center mt-10">
            <div className="text-left p-3 w-[75%]">
                <h1 className="mb-4">{t('labels')}</h1>
                <div className="flex bg-slate-500">
                    <table className='text-center table-auto w-full bg-red-200' id='table'>
                        <thead>
                            <tr>
                                <th>{t('labels')}</th>
                                <th>{t('confidence')}</th>
                            </tr>
                        </thead>
                        <tbody>
                            {isValidResponse && response.map((label, index) => (
                                <tr key={index}>
                                    <td>{label.Name}</td>
                                    <td>{label.Confidence}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
}
