const BACKEND_URI = "";

import { SimpleAPIResponse } from "./models";

export async function getHeaders(idToken: string | undefined): Promise<Record<string, string>> {
    // If using login and not using app services, add the id token of the logged in account as the authorization
    return {};
}

export async function configApi(): Promise<SimpleAPIResponse> {
    const response = await fetch(`${BACKEND_URI}/config`, {
        method: "GET"
    });

    return (await response.json()) as SimpleAPIResponse;
}
