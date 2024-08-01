import styles from "./Chat.module.css";

const Chat = () => {
    return (
        <div className={styles.container}>
            <div className={styles.chatRoot}>
                <div className={styles.chatContainer}>
                        <div className={styles.chatEmptyState}>
                            <h1 className={styles.chatEmptyStateTitle}>Chat with your data</h1>
                            <h2 className={styles.chatEmptyStateSubtitle}>Ask anything or try an example</h2>
                        </div>
                </div>
            </div>
        </div>
    );
};

export default Chat;
