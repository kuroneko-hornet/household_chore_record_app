import { AccountInfo, EventType, PublicClientApplication } from "@azure/msal-browser";
// import { checkLoggedIn, msalConfig, useLogin } from "./authConfig";
import { useEffect, useState } from "react";
import { MsalProvider } from "@azure/msal-react";
import Layout from "./pages/layout/Layout";

const LayoutWrapper = () => {
    const [loggedIn, setLoggedIn] = useState(false);
    return (
        <Layout />
    );
};

export default LayoutWrapper;
